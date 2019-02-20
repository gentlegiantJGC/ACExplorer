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

		qt = QtWidgets.QApplication(sys.argv)
		self.main_window = QtWidgets.QMainWindow()

		self.main_window.setObjectName("MainWindow")
		self.main_window.resize(809, 698)
		self.centralwidget = QtWidgets.QWidget(self.main_window)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.comboBox = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.horizontalLayout_2.addWidget(self.comboBox)
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_2.addWidget(self.lineEdit)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
		self.treeWidget.setObjectName("treeWidget")
		item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
		self.horizontalLayout.addWidget(self.treeWidget)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.main_window.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(self.main_window)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.main_window.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self.main_window)
		self.statusbar.setObjectName("statusbar")
		self.main_window.setStatusBar(self.statusbar)
		self.actionOptions = QtWidgets.QAction(self.main_window)
		self.actionOptions.setObjectName("actionOptions")
		self.menuFile.addAction(self.actionOptions)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(self.main_window)
		QtCore.QMetaObject.connectSlotsByName(self.main_window)

		self.main_window.show()
		sys.exit(qt.exec_())

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "ACExplorer", None, -1))
		self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "ACU", None, -1))
		self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
		__sortingEnabled = self.treeWidget.isSortingEnabled()
		self.treeWidget.setSortingEnabled(False)
		self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "ACU", None, -1))
		self.treeWidget.setSortingEnabled(__sortingEnabled)
		self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
		self.actionOptions.setText(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))


if __name__ == "__main__":
	import sys
	app = App()

