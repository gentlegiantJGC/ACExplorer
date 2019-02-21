"""
	This is an explorer for the forge file format used in a number of Ubisoft games mainly consisting
	of the Assassin's Creed franchise. 	This is just a UI wrapper for pyUbiForge where the heavy lifting is done.
"""

import pyUbiForge
from typing import Union
from PySide2 import QtCore, QtGui, QtWidgets


class App(QtWidgets.QApplication):
	"""This is the main application that contains the file tree.
	This class also sets up pyUbiForge.
	"""
	def __init__(self):
		QtWidgets.QApplication.__init__(self)
		self.pyUbiForge = pyUbiForge.PyUbiForgeMain()
		self.log = self.pyUbiForge.log
		self.log.info(__name__, 'Building GUI Window')

		# set up main window
		self.main_window = QtWidgets.QMainWindow()
		self.main_window.setObjectName("MainWindow")
		self.main_window.setWindowIcon(QtGui.QIcon('icon.ico'))
		self.main_window.resize(809, 698)
		self.central_widget = QtWidgets.QWidget(self.main_window)
		self.central_widget.setObjectName("centralwidget")
		self.main_window.setCentralWidget(self.central_widget)
		self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
		self.vertical_layout.setObjectName("verticalLayout")
		self.horizontal_layout = QtWidgets.QHBoxLayout()
		self.horizontal_layout.setObjectName("horizontal_layout")
		self.vertical_layout.addLayout(self.horizontal_layout)

		# drop down box to select the game
		self.game_select = QtWidgets.QComboBox(self.central_widget)
		self.game_select.setObjectName("game_select")
		for game_identifier in self.pyUbiForge.game_identifiers:
			self.game_select.addItem(game_identifier)
		self.horizontal_layout.addWidget(self.game_select)

		# search box
		self.search_box = QtWidgets.QLineEdit(self.central_widget)
		self.search_box.setObjectName("search_box")
		self.search_box.editingFinished.connect(self.search)
		self.horizontal_layout.addWidget(self.search_box)

		# file tree view
		self.file_view = TreeView(self.pyUbiForge, self.central_widget)
		self.file_view.setObjectName("file_view")
		self.vertical_layout.addWidget(self.file_view)

		# menu options
		self.menubar = QtWidgets.QMenuBar(self.main_window)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
		self.menubar.setObjectName("menubar")
		self.file_menu = QtWidgets.QMenu(self.menubar)
		self.file_menu.setObjectName("file_menu")
		self.main_window.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self.main_window)
		self.statusbar.setObjectName("statusbar")
		self.main_window.setStatusBar(self.statusbar)
		# self.statusbar.showMessage('hi')
		self.options_button = QtWidgets.QAction(self.main_window)
		self.options_button.setObjectName("actionOptions")
		self.file_menu.addAction(self.options_button)
		self.menubar.addAction(self.file_menu.menuAction())

		self.translate_()
		# QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.main_window.show()
		self.load_game(self.game_select.currentText())
		self.exec_()

	def translate_(self):
		self.main_window.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ACExplorer"))
		self.file_menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "File"))
		self.options_button.setText(QtWidgets.QApplication.translate("MainWindow", "Options"))
		self.file_view.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Name"))

	def load_game(self, game_identifier: str):
		"""Tell pyUbiForge to load the new game and populate the file tree with the data it gives."""

		self.pyUbiForge.load_game(game_identifier)
		self.file_view.setUpdatesEnabled(False)
		self.file_view.load_game(game_identifier)

		for forge_file_name, forge_file in self.pyUbiForge.forge_files.items():
			self.file_view.insert(forge_file_name, forge_file_name)
			for datafile_id, datafile in forge_file.datafiles.items():
				self.file_view.insert(datafile.file_name, forge_file_name, datafile_id)

		self.file_view.setUpdatesEnabled(True)

	def search(self):
		self.file_view.search(self.search_box.text())


class TreeView(QtWidgets.QTreeWidget):
	"""This is the file tree used in the main application.
	Wraps QTreeWidget and adds search functionality and a context menu
	"""
	def __init__(self, py_ubi_forge, parent):
		QtWidgets.QTreeWidget.__init__(self, parent)
		self.pyUbiForge = py_ubi_forge
		self._entries = {}
		self._game_identifier = None
		self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.customContextMenuRequested.connect(self.open_context_menu)

	def load_game(self, game_identifier: str):
		self._entries.clear()
		# TODO: check that this removes entries from the tree
		self._game_identifier = game_identifier
		self.insert(game_identifier)

	def search(self, search_string: str) -> None:
		self._entries[(None, None, None)].search(search_string)

	def insert(self, entry_name: str, forge_file_name: str = None, datafile_id: int = None, file_id: int = None) -> None:
		if forge_file_name is not None:
			if datafile_id is not None:
				if file_id is not None:  # the fact that the ends of these align makes me very happy
					parent = self._entries[(forge_file_name, datafile_id, None)]
				else:
					parent = self._entries[(forge_file_name, None, None)]
			else:
				parent = self._entries[(None, None, None)]
			entry = TreeViewEntry(self.pyUbiForge, parent, entry_name, forge_file_name, datafile_id, file_id)
		else:
			entry = TreeViewEntry(self.pyUbiForge, self, entry_name)

		self._entries[(forge_file_name, datafile_id, file_id)] = entry

	def open_context_menu(self, position):
		entry: TreeViewEntry = self.itemAt(position)
		if entry is not None:
			unique_identifier = (None, entry.forge_file_name, entry.datafile_id, entry.file_id)[entry.depth]
			plugin_names, file_id = self.pyUbiForge.right_click_plugins.query(entry.depth, unique_identifier, entry.forge_file_name, entry.datafile_id)

			menu = ContextMenu(self.pyUbiForge, plugin_names, file_id, entry.forge_file_name, entry.datafile_id)
			menu.exec_(self.viewport().mapToGlobal(position))


class TreeViewEntry(QtWidgets.QTreeWidgetItem):
	"""Individual entries in the file tree.
	Wraps QTreeWidgetItem and saves more data related to each entry
	"""
	def __init__(self, py_ubi_forge, tree_view, entry_name: str, forge_file_name: str = None, datafile_id: int = None, file_id: int = None):
		QtWidgets.QTreeWidgetItem.__init__(self, tree_view, [entry_name])
		self.pyUbiForge = py_ubi_forge
		self._entry_name = entry_name
		self._forge_file_name = forge_file_name
		self._datafile_id = datafile_id
		self._file_id = file_id
		self._dev_search = None
		self._depth = None

	@property
	def entry_name(self):
		return self._entry_name

	@property
	def forge_file_name(self):
		return self._forge_file_name

	@property
	def datafile_id(self):
		return self._datafile_id

	@property
	def file_id(self):
		return self._file_id

	@property
	def dev_search(self):
		if self._dev_search is None:
			self._dev_search = [f'{attr:016X}' for attr in [self.datafile_id, self.file_id] if attr is not None]
			self._dev_search += [''.join(attr[n:n + 2] for n in reversed(range(0, 16, 2))) for attr in self._dev_search]
		return self._dev_search

	@property
	def depth(self):
		if self._depth is None:
			if self.forge_file_name is not None:
				if self.datafile_id is not None:
					if self.file_id is not None:
						self._depth = 4
					else:
						self._depth = 3
				else:
					self._depth = 2
			else:
				self._depth = 1
		return self._depth

	def search(self, search_string: str) -> bool:
		if search_string == '' or any(search_string in attr for attr in [self._entry_name, self._forge_file_name] if attr is not None):
			# if the string is empty or matches one of the parameters unhide self and children.
			self.recursively_unhide_children()
			return True
		elif self.pyUbiForge.CONFIG['dev'] and any(search_string in attr for attr in self.dev_search):
			# if in dev mode and matches one of the file ids unhide self and children
			self.recursively_unhide_children()
			return True
		else:
			shown = any([self.child(index).search(search_string) for index in range(self.childCount())])
			self.setHidden(not shown)
			return shown

	def recursively_unhide_children(self):
		self.setHidden(False)
		for index in range(self.childCount()):
			self.child(index).recursively_unhide_children()


class ContextMenu(QtWidgets.QMenu):
	"""Context menu for use upon right click of an item in the file tree to access the plugin system."""
	def __init__(self, py_ubi_forge, plugin_names, file_id, forge_file_name, datafile_id):
		QtWidgets.QMenu.__init__(self)
		self.pyUbiForge = py_ubi_forge
		for plugin_name in plugin_names:
			self.add_command(plugin_name, file_id, forge_file_name, datafile_id)

	def add_command(self, plugin_name: str, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None):
		"""Workaround for plugin in post method getting overwritten which lead to all options calling the last plugin."""
		self.addAction(
			plugin_name,
			lambda: self.run_plugin(plugin_name, file_id, forge_file_name, datafile_id)
		)

	def run_plugin(self, plugin_name: str, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None) -> None:
		"""Method to run and handle plugin options."""
		options = []
		while options is not None:
			options, output = self.pyUbiForge.right_click_plugins.run(plugin_name, file_id, forge_file_name, datafile_id, options)
			# TODO: show options screen, wait for response from option screen


if __name__ == "__main__":
	app = App()
	app.pyUbiForge.save()
