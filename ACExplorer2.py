"""
	This is an explorer for the forge file format used in a number of Ubisoft games mainly consisting
	of the Assassin's Creed franchise. 	This is just a UI wrapper for pyUbiForge where the heavy lifting is done.
"""

from typing import Union
import pyUbiForge
from PySide2 import QtCore, QtGui, QtWidgets
import sys


class TreeView(QtWidgets.QTreeWidget):
	def __init__(self, py_ubi_forge, parent):
		QtWidgets.QTreeWidget.__init__(self, parent)
		self.pyUbiForge = py_ubi_forge
		self._entries = {}
		self._game_identifier = None

	def load_game(self, game_identifier: str):
		self._entries.clear()
		# TODO: check that this removes entries from the tree
		self._game_identifier = game_identifier
		self.insert(game_identifier)
		# TODO: populate the forge files and datafiles

	def search(self, search_string: str) -> None:
		self._entries[(None, None, None)].search(search_string)

	def insert(self, entry_name: str, forge_file_name: str = None, datafile_id: int = None, file_id: int = None):
		entry = TreeViewEntry(self.pyUbiForge, self, entry_name, forge_file_name, datafile_id, file_id)
		self._entries[(forge_file_name, datafile_id, file_id)] = entry
		if forge_file_name is not None:
			if datafile_id is not None:
				if file_id is not None:  # the fact that the ends of these align makes me very happy
					self._entries[(forge_file_name, datafile_id, None)].addChild(entry)
				else:
					self._entries[(forge_file_name, None, None)].addChild(entry)
			else:
				self._entries[(None, None, None)].addChild(entry)


class TreeViewEntry(QtWidgets.QTreeWidgetItem):
	def __init__(self, py_ubi_forge, tree_view, entry_name: str, forge_file_name: str = None, datafile_id: int = None, file_id: int = None):
		QtWidgets.QTreeWidgetItem.__init__(self, tree_view)
		self.pyUbiForge = py_ubi_forge
		self._entry_name = entry_name
		self.setText(0, entry_name)
		self._forge_file_name = forge_file_name
		self._datafile_id = datafile_id
		self._file_id = file_id
		self._dev_search = [f'{attr:016X}' for attr in [datafile_id, file_id] if attr is not None]
		self._dev_search += [''.join(attr[n:n+2] for n in reversed(range(0, 16, 2))) for attr in self._dev_search]

	def search(self, search_string: str) -> bool:
		if search_string == '' or any(search_string in attr for attr in [self._entry_name, self._forge_file_name]):
			# if the string is empty or matches one of the parameters unhide self and children.
			self.recursively_unhide_children()
			return True
		elif self.pyUbiForge.CONFIG['dev'] and any(search_string in attr for attr in self._dev_search):
			# if in dev mode and matches one of the file ids unhide self and children
			self.recursively_unhide_children()
			return True
		else:
			shown = any([child.search(search_string) for child in self._children])
			self.setHidden(not shown)
			return shown

	def recursively_unhide_children(self):
		self.setHidden(False)
		for index in range(self.childCount()):
			self.child(index).recursively_unhide_children()



class App(QtWidgets.QApplication):
	"""This is the class that contains all the UI features for ACExplorer.

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
		self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
		self.vertical_layout.setObjectName("verticalLayout")
		self.horizontal_layout = QtWidgets.QHBoxLayout()
		self.horizontal_layout.setObjectName("horizontal_layout")

		# drop down box to select the game
		self.game_select = QtWidgets.QComboBox(self.central_widget)
		self.game_select.setObjectName("game_select")
		for game_identifier in self.pyUbiForge.game_identifiers:
			self.game_select.addItem(game_identifier)
		self.horizontal_layout.addWidget(self.game_select)

		# search box
		self.search_box = QtWidgets.QLineEdit(self.central_widget)
		self.search_box.setObjectName("search_box")
		self.horizontal_layout.addWidget(self.search_box)
		self.vertical_layout.addLayout(self.horizontal_layout)

		# file tree view
		self.file_view = TreeView(self.pyUbiForge, self.central_widget)
		self.file_view.setObjectName("file_view")
		self.file_view.load_game(self.game_select.currentText())
		self.vertical_layout.addWidget(self.file_view)

		# add the central widget
		self.main_window.setCentralWidget(self.central_widget)

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
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.main_window.show()
		sys.exit(self.exec_())

	def translate_(self):
		self.main_window.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ACExplorer"))
		__sortingEnabled = self.file_view.isSortingEnabled()
		self.file_view.setSortingEnabled(False)
		self.file_view.setSortingEnabled(__sortingEnabled)
		self.file_menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "File"))
		self.options_button.setText(QtWidgets.QApplication.translate("MainWindow", "Options"))


if __name__ == "__main__":
	app = App()

