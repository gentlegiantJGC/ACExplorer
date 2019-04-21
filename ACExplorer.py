"""
	This is an explorer for the forge file format used in a number of Ubisoft games mainly consisting
	of the Assassin's Creed franchise. 	This is just a UI wrapper for pyUbiForge where the heavy lifting is done.
"""

import pyUbiForge
from typing import Union, Dict, List, Tuple
from PySide2 import QtCore, QtGui, QtWidgets
import time
import os
import json
import sys
import subprocess


class App(QtWidgets.QApplication):
	"""This is the main application that contains the file tree.
	This class also sets up pyUbiForge.
	"""
	def __init__(self):
		QtWidgets.QApplication.__init__(self)
		self.pyUbiForge = pyUbiForge.PyUbiForgeMain()
		self.log = self.pyUbiForge.log
		self.log.info(__name__, 'Building GUI Window')

		# load the style
		self.icons = {}

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
		self.game_select = QtWidgets.QComboBox()
		self.game_select.setObjectName("game_select")
		self.game_select.addItems(self.pyUbiForge.game_identifiers)
		self.horizontal_layout.addWidget(self.game_select)

		# search box
		self._last_search = ''
		self.search_box = QtWidgets.QLineEdit()
		self.search_box.setObjectName("search_box")
		self.search_box.editingFinished.connect(self.search)
		self.horizontal_layout.addWidget(self.search_box)

		# file tree view
		self.file_view = TreeView(self.pyUbiForge, self.central_widget, self.icons)
		self.file_view.setObjectName("file_view")
		self.file_view.setHeaderHidden(True)
		self.vertical_layout.addWidget(self.file_view)

		default_options = {
			"style": 'QDarkStyle'
		}

		try:
			with open('config.json') as config:
				self._options = json.load(config)
			for key, val in default_options:
				if key not in self._options:
					self._options[key] = val
		except:
			self._options = default_options

		# menu options
		self.menubar = QtWidgets.QMenuBar()
		self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
		self.menubar.setObjectName("menubar")
		self.main_window.setMenuBar(self.menubar)

		self.menubar.addAction(
			'Games',
			lambda: self._show_games()
		)

		self.menubar.addAction(
			'Options',
			lambda: self._show_options()
		)

		self.menubar.addAction(
			'Donate',
			lambda: self._donate()
		)

		# statusbar
		self.statusbar = StatusBar(self.main_window, self.log)
		self.statusbar.setObjectName("statusbar")
		self.main_window.setStatusBar(self.statusbar)
		self.statusbar.start()

		self.load_style(self._options['style'])

		self.translate_()
		# QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.main_window.show()
		self.load_game(self.game_select.currentText())
		self.exec_()

	def translate_(self):
		self.main_window.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ACExplorer"))

	def load_game(self, game_identifier: str):
		"""Tell pyUbiForge to load the new game and populate the file tree with the data it gives."""
		self.processEvents()

		for _ in self.pyUbiForge.load_game(game_identifier):
			self.processEvents()

		self.file_view.load_game(game_identifier)

		for forge_file_name, forge_file in self.pyUbiForge.forge_files.items():
			self.pyUbiForge.log.info(__name__, f'Populating File Tree For {forge_file_name}')
			self.file_view.insert(forge_file_name, forge_file_name, icon=self.icons.get('unknown_file', None))
			for datafile_id, datafile in sorted(forge_file.datafiles.items(), key=lambda v: v[1].file_name.lower()):
				self.file_view.insert(datafile.file_name, forge_file_name, datafile_id, icon=self.icons.get(f'{datafile.file_type:08X}', None))
			self.processEvents()
		self.pyUbiForge.log.info(__name__, 'Finished Populating File Tree')
		self.pyUbiForge.log.info(__name__, '')

	def save(self):
		self.pyUbiForge.save()
		with open('config.json', 'w') as config:
			json.dump(self._options, config)

	def search(self):
		if self.search_box.text() != self._last_search:
			self._last_search = self.search_box.text()
			self.file_view.search(self.search_box.text())

	def load_style(self, style_name: str):
		with open(f'./resources/themes/{style_name}/style.qss') as style:
			self.setStyleSheet(style.read())
		for icon in os.listdir('resources/icons'):
			self.icons[os.path.splitext(icon)[0]] = QtGui.QIcon(f'resources/icons/{icon}')
		if os.path.isdir(f'resources/themes/{style_name}/icons'):
			for icon in os.listdir(f'resources/themes/{style_name}/icons'):
				self.icons[os.path.splitext(icon)[0]] = QtGui.QIcon(f'resources/themes/{style_name}/icons/{icon}')
		self._options['style'] = style_name

	def _show_games(self):
		current_game_path = self.pyUbiForge.CONFIG.game_folder(self.game_select.currentText())
		screen = PluginOptionsScreen(
			self.pyUbiForge,
			'Game Paths',
			{
				game_identifier: {
					'type': 'dir_select',
					'default': game_path
				} for game_identifier, game_path in self.pyUbiForge.CONFIG.get('gameFolders', {}).items()
			}
		)
		if not screen.escape:
			self.pyUbiForge.CONFIG['gameFolders'] = screen.options
			if self.pyUbiForge.CONFIG.game_folder(self.game_select.currentText()) != current_game_path:
				self.load_game(self.game_select.currentText())

	def _show_options(self):
		screen = PluginOptionsScreen(
			self.pyUbiForge,
			'Options',
			{
				'Missing Texture Path': {
					'type': 'file_select',
					'default': self.pyUbiForge.CONFIG.get('missingNo', 'resources/missingNo.png')
				},
				'Default Output Folder': {
					'type': 'dir_select',
					'default': self.pyUbiForge.CONFIG.get('dumpFolder', 'output')
				},
				'Log File': {
					'type': 'file_select',
					'default': self.pyUbiForge.CONFIG.get('logFile', 'ACExplorer.log')
				},
				'Temporary Files Memory Buffer (MB)': {
					'type': 'int_entry',
					'default': self.pyUbiForge.CONFIG.get('tempFilesMaxMemoryMB', 2048),
					"min": 50
				},
				'Style': {
					'type': "select",
					"options": [
						theme for theme in os.listdir('./resources/themes') if os.path.isdir(f'./resources/themes/{theme}') and os.path.isfile(f'./resources/themes/{theme}/style.qss')
					]
				}
			}
		)
		options = screen.options
		if not screen.escape:
			self.pyUbiForge.CONFIG['missingNo'] = options['Missing Texture Path']
			self.pyUbiForge.CONFIG['dumpFolder'] = options['Default Output Folder']
			self.pyUbiForge.CONFIG['logFile'] = options['Log File']
			self.pyUbiForge.CONFIG['tempFilesMaxMemoryMB'] = options['Temporary Files Memory Buffer (MB)']
			if self._options['style'] != options['Style']:
				self._options['style'] = options['Style']
				self.load_style(self._options['style'])

	@staticmethod
	def _donate():
		if sys.platform == 'win32':
			os.startfile('https://www.paypal.me/gentlegiantJGC')
		elif sys.platform == 'darwin':
			subprocess.Popen(['open', 'https://www.paypal.me/gentlegiantJGC'])
		else:
			try:
				subprocess.Popen(['xdg-open', 'https://www.paypal.me/gentlegiantJGC'])
			except OSError:
				pass


class StatusBar(QtWidgets.QStatusBar, QtCore.QThread):
	def __init__(self, parent: QtWidgets.QMainWindow, log: pyUbiForge.misc.log.Logger):
		QtWidgets.QStatusBar.__init__(self, parent)
		QtCore.QThread.__init__(self)
		self.log = log

	def run(self):
		while True:
			if self.log.buffer is not None:
				self.showMessage(self.log.buffer)
				self.log.buffer = None
			time.sleep(0.02)


class TreeView(QtWidgets.QTreeWidget):
	"""This is the file tree used in the main application.
	Wraps QTreeWidget and adds search functionality and a context menu
	"""
	def __init__(self, py_ubi_forge: pyUbiForge.PyUbiForgeMain, parent: QtWidgets.QWidget, icons: Dict[str, QtGui.QIcon]):
		QtWidgets.QTreeWidget.__init__(self, parent)
		self.icons = icons
		self.pyUbiForge = py_ubi_forge
		self._entries: Dict[Tuple[Union[None, str], Union[None, int], Union[None, int]], TreeViewEntry] = {}
		self._game_identifier = None
		self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.customContextMenuRequested.connect(self.open_context_menu)

	def load_game(self, game_identifier: str):
		self._entries.clear()
		self.clear()
		self._game_identifier = game_identifier
		self.insert(game_identifier, icon=self.icons['directory'])

	def search(self, search_string: str) -> None:
		self._entries[(None, None, None)].search(search_string)

	def insert(self, entry_name: str, forge_file_name: str = None, datafile_id: int = None, file_id: int = None, icon: QtGui.QIcon = None) -> None:
		if forge_file_name is not None:
			if datafile_id is not None:
				if file_id is not None:  # the fact that the ends of these align makes me very happy
					parent = self._entries[(forge_file_name, datafile_id, None)]
				else:
					parent = self._entries[(forge_file_name, None, None)]
			else:
				parent = self._entries[(None, None, None)]
			entry = TreeViewEntry(self.pyUbiForge, parent, entry_name, forge_file_name, datafile_id, file_id, icon=icon)
			parent.addChild(entry)
		else:
			entry = TreeViewEntry(self.pyUbiForge, self, entry_name, icon=icon)

		self._entries[(forge_file_name, datafile_id, file_id)] = entry

	def populate_tree(self):
		"""A helper function to populate files in the file view."""
		for forge_file_name, forge_file in self.pyUbiForge.forge_files.items():
			for datafile_id in forge_file.new_datafiles:
				for file_id, file_name in sorted(forge_file.datafiles[datafile_id].files.items(), key=lambda v: v[1].lower()):
					self.insert(
						file_name,
						forge_file_name,
						datafile_id,
						file_id,
						icon=self.icons.get(
							self.pyUbiForge.temp_files(file_id, forge_file_name, datafile_id).file_type,
							None
						)
					)
			forge_file.new_datafiles.clear()

	def mousePressEvent(self, event: QtGui.QMouseEvent):
		entry: TreeViewEntry = self.itemAt(event.pos())
		if entry is not None and entry.depth == 3 and entry.childCount() == 0:
			forge_file_name, datafile_id = entry.forge_file_name, entry.datafile_id
			self.pyUbiForge.forge_files[forge_file_name].decompress_datafile(datafile_id)
			self.populate_tree()
		QtWidgets.QTreeWidget.mousePressEvent(self, event)

	def open_context_menu(self, position: QtCore.QPoint):
		entry: TreeViewEntry = self.itemAt(position)
		if entry is not None:
			unique_identifier = (None, entry.forge_file_name, entry.datafile_id, entry.file_id)[entry.depth-1]
			plugin_names, file_id = self.pyUbiForge.right_click_plugins.query(entry.depth, unique_identifier, entry.forge_file_name, entry.datafile_id)

			menu = ContextMenu(self.pyUbiForge, self.icons, plugin_names, file_id, entry.forge_file_name, entry.datafile_id)
			menu.exec_(self.viewport().mapToGlobal(position))
			self.populate_tree()


class TreeViewEntry(QtWidgets.QTreeWidgetItem):
	"""Individual entries in the file tree.
	Wraps QTreeWidgetItem and saves more data related to each entry
	"""
	def __init__(self, py_ubi_forge: pyUbiForge.PyUbiForgeMain, tree_view: Union[TreeView, 'TreeViewEntry'], entry_name: str, forge_file_name: str = None, datafile_id: int = None, file_id: int = None, icon: QtGui.QIcon = None):
		QtWidgets.QTreeWidgetItem.__init__(self, tree_view, [entry_name])
		if icon is not None:
			self.setIcon(0, icon)
		self.pyUbiForge = py_ubi_forge
		self._entry_name = entry_name
		self._forge_file_name = forge_file_name
		self._datafile_id = datafile_id
		self._file_id = file_id
		self._dev_search = None
		self._depth = None

	@property
	def entry_name(self) -> str:
		return self._entry_name

	@property
	def forge_file_name(self) -> Union[str, None]:
		return self._forge_file_name

	@property
	def datafile_id(self) -> Union[int, None]:
		return self._datafile_id

	@property
	def file_id(self) -> Union[int, None]:
		return self._file_id

	@property
	def dev_search(self) -> List[str]:
		if self._dev_search is None:
			self._dev_search = [f'{attr:016X}' for attr in [self.datafile_id, self.file_id] if attr is not None]
			self._dev_search += [''.join(attr[n:n + 2] for n in reversed(range(0, 16, 2))) for attr in self._dev_search]
		return self._dev_search

	@property
	def depth(self) -> int:
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
		elif self.pyUbiForge.CONFIG.get('dev', False) and any(search_string.upper() in attr for attr in self.dev_search):
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
	def __init__(self, py_ubi_forge: pyUbiForge.PyUbiForgeMain, icons: Dict[str, QtGui.QIcon], plugin_names: List[str], file_id: Union[str, int], forge_file_name: Union[None, str], datafile_id: Union[None, int]):
		QtWidgets.QMenu.__init__(self)
		self.pyUbiForge = py_ubi_forge
		self.icons = icons

		for plugin_name in sorted(plugin_names):
			self.add_command(plugin_name, file_id, forge_file_name, datafile_id)

	def add_command(self, plugin_name: str, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None):
		"""Workaround for plugin in post method getting overwritten which lead to all options calling the last plugin."""
		if self.pyUbiForge.right_click_plugins.get_screen_options(plugin_name, []) is None:
			self.addAction(
				plugin_name,
				lambda: self.run_plugin(plugin_name, file_id, forge_file_name, datafile_id)
			)
		else:
			self.addAction(
				self.icons.get('context_right_click_icon', None),
				plugin_name,
				lambda: self.run_plugin(plugin_name, file_id, forge_file_name, datafile_id)
			)

	def run_plugin(self, plugin_name: str, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None) -> None:
		"""Method to run and handle plugin options."""
		self.pyUbiForge.right_click_plugins.run(plugin_name, file_id, forge_file_name, datafile_id)

	def mousePressEvent(self, event: QtGui.QMouseEvent):
		if event.button() == QtCore.Qt.RightButton:
			entry = self.actionAt(event.pos())
			if entry is not None:
				plugin_name = entry.text()
				options = []
				escape = False
				new_screen = self.pyUbiForge.right_click_plugins.get_screen_options(plugin_name, options)
				while new_screen is not None and not escape:
					# show screen
					screen = PluginOptionsScreen(self.pyUbiForge, plugin_name, new_screen)
					escape = screen.escape
					if not escape:
						# pull options from screen
						options.append(screen.options)
						new_screen = self.pyUbiForge.right_click_plugins.get_screen_options(plugin_name, options)
				if not escape:
					entry.trigger()
			else:
				QtWidgets.QMenu.mousePressEvent(self, event)
		elif event.button() == QtCore.Qt.LeftButton:
			QtWidgets.QMenu.mousePressEvent(self, event)


class PluginOptionsScreen(QtWidgets.QDialog):
	def __init__(self, py_ubi_forge: pyUbiForge.PyUbiForgeMain, plugin_name: str, screen: Dict[str, dict]):
		QtWidgets.QDialog.__init__(self)
		self._pyUbiForge = py_ubi_forge
		self.setModal(True)
		self._screen = screen
		self._options = {}
		self._labels = []
		self._escape = False
		self.setWindowTitle(plugin_name)
		self.setWindowIcon(QtGui.QIcon('icon.ico'))

		self._vertical_layout = QtWidgets.QVBoxLayout()
		self._vertical_layout.setObjectName("verticalLayout")
		self.setLayout(self._vertical_layout)

		self._horizontal_layouts = []

		for option_name, option in screen.items():
			option_type = option.get('type', None)
			self._horizontal_layouts.append(QtWidgets.QHBoxLayout())
			self._vertical_layout.addLayout(self._horizontal_layouts[-1])
			self._labels.append(QtWidgets.QLabel())
			self._labels[-1].setText(option_name)
			self._horizontal_layouts[-1].addWidget(self._labels[-1])
			if option_type == 'select':
				selection = [str(op) for op in option.get('options', [])]
				self._options[option_name] = QtWidgets.QComboBox()
				self._options[option_name].addItems(selection)
				self._horizontal_layouts[-1].addWidget(self._options[option_name])
			elif option_type == 'str_entry':
				self._options[option_name] = QtWidgets.QLineEdit()
				self._options[option_name].setText(option.get('default', ''))
				self._horizontal_layouts[-1].addWidget(self._options[option_name])
			elif option_type == 'int_entry':
				self._options[option_name] = QtWidgets.QSpinBox()
				val = option.get('default', 0)
				if not isinstance(val, int):
					val = 0
				if isinstance(option.get('min', None), int):
					self._options[option_name].setMinimum(option.get('min'))
				else:
					self._options[option_name].setMinimum(-999999999)
				if isinstance(option.get('max', None), int):
					self._options[option_name].setMaximum(option.get('max'))
				else:
					self._options[option_name].setMaximum(999999999)
				self._options[option_name].setValue(val)
				self._horizontal_layouts[-1].addWidget(self._options[option_name])
			elif option_type == 'float_entry':
				self._options[option_name] = QtWidgets.QDoubleSpinBox()
				self._options[option_name].setDecimals(10)
				val = option.get('default', 0.0)
				if isinstance(val, int):
					val = float(val)
				elif not isinstance(val, float):
					val = 0.0
				if isinstance(option.get('min', None), (int, float)):
					self._options[option_name].setMinimum(float(option.get('min')))
				else:
					self._options[option_name].setMinimum(float('-Inf'))
				if isinstance(option.get('max', None), (int, float)):
					self._options[option_name].setMaximum(float(option.get('max')))
				else:
					self._options[option_name].setMaximum(float('Inf'))
				self._options[option_name].setValue(val)
				self._horizontal_layouts[-1].addWidget(self._options[option_name])
			elif option_name == 'check_box':
				self._options[option_name] = QtWidgets.QCheckBox()
				self._options[option_name].setChecked(option.get('default', True))
				self._horizontal_layouts[-1].addWidget(self._options[option_name])
			elif option_type == 'dir_select':
				self.create_dialog_button(option_name, option, 'dir')
			elif option_type == 'file_select':
				self.create_dialog_button(option_name, option, 'file')

		self._horizontal_layouts.append(QtWidgets.QHBoxLayout())
		self._vertical_layout.addLayout(self._horizontal_layouts[-1])
		self._vertical_layout.addLayout(self._horizontal_layouts[-1])

		self._okay_button = QtWidgets.QPushButton('OK')
		self._okay_button.clicked.connect(lambda: self.done(1))
		self._cancel_button = QtWidgets.QPushButton('Cancel')
		self._cancel_button.clicked.connect(self.reject)
		self._horizontal_layouts[-1].addWidget(self._okay_button)
		self._horizontal_layouts[-1].addWidget(self._cancel_button)

		self.show()
		self.exec_()

	def reject(self):
		self._escape = True
		QtWidgets.QDialog.reject(self)

	@property
	def options(self) -> Dict[str, Union[str, int, float]]:
		options = {}
		for option_name, var in self._options.items():
			if isinstance(var, QtWidgets.QComboBox):
				options[option_name] = self._screen[option_name]['options'][var.currentIndex()]
			elif isinstance(var, QtWidgets.QLineEdit):
				options[option_name] = var.text()
			elif isinstance(var, QtWidgets.QSpinBox):
				options[option_name] = var.value()
			elif isinstance(var, QtWidgets.QDoubleSpinBox):
				options[option_name] = var.value()
			elif isinstance(var, QtWidgets.QCheckBox):
				options[option_name] = var.isChecked()
			elif isinstance(var, QtWidgets.QPushButton):
				options[option_name] = var.text()
		return options

	@property
	def escape(self) -> bool:
		return self._escape

	def create_dialog_button(self, option_name: str, option: dict, mode: str):
		self._options[option_name] = QtWidgets.QPushButton()
		if "default" in option and isinstance(option["default"], str):
			path = option["default"]
		else:
			path = self._pyUbiForge.CONFIG.get("dumpFolder")
		self._options[option_name].setText(path)
		self._options[option_name].clicked.connect(lambda: self.open_dialog(option_name, mode, path))
		self._horizontal_layouts[-1].addWidget(self._options[option_name])

	def open_dialog(self, option_name: str, mode: str, path: str):
		text = None
		if mode == 'dir':
			text = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory", path)
		elif mode == 'file':
			text = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", path)
			if text != '':
				text = text[0]

		if text != '':
			self._options[option_name].setText(text)


if __name__ == "__main__":
	app = App()
	app.save()
