"""
	This is an explorer for the forge file format used in a number of Ubisoft games mainly consisting
	of the Assassin's Creed franchise. 	This is just a UI wrapper for pyUbiForge where the heavy lifting is done.
"""

from typing import Union
import pyUbiForge
from PySide2 import QtCore, QtGui, QtWidgets


class App:
	"""This is the class that contains all the UI features for ACExplorer.

	This class also sets up pyUbiForge.
	"""
	def __init__(self):
		self.pyUbiForge = pyUbiForge.PyUbiForgeMain()
		self.log = self.pyUbiForge.log
		self.log.info(__name__, 'Building GUI Window')

		# set up main window
		qt = QtWidgets.QApplication(sys.argv)
		self.main_window = QtWidgets.QMainWindow()
		self.main_window.setObjectName("MainWindow")
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
		self.file_view = QtWidgets.QTreeWidget(self.central_widget)
		self.file_view.setObjectName("file_view")
		item_0 = QtWidgets.QTreeWidgetItem(self.file_view)
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

		self.translate()
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.main_window.show()
		sys.exit(qt.exec_())

	def translate(self):
		self.main_window.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ACExplorer"))
		self.game_select.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "ACU"))
		self.file_view.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1"))
		__sortingEnabled = self.file_view.isSortingEnabled()
		self.file_view.setSortingEnabled(False)
		self.file_view.setSortingEnabled(__sortingEnabled)
		self.file_menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "File"))
		self.options_button.setText(QtWidgets.QApplication.translate("MainWindow", "Options"))


if __name__ == "__main__":
	import sys
	app = App()

