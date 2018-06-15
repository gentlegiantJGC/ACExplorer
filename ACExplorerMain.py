'''
	This is an explorer for the forge file format used in Assassin's Creed
	The format varies slightly between games and the current implementation will only work
	with Assassin's Creed Unity.
	The forge file format is similar to a zip file in concept however each individual containing
	file can be decompressed individually.
	The 'folders' in the top level of the forge file will from this point on be referred to as datafiles.
	Contained within the datafiles are a variety of files related to that datafile.
'''

import json, ttk, Tkinter, sys
from ACExplorer import CONFIG
from ACExplorer.misc import log, tempFiles
from ACExplorer.ACUnity.decompressDatafile import decompressDatafile
from ACExplorer.ACUnity.readFile import readFile
from ACExplorer.ACUnity.readForge import readForge

dev = 'dev' in sys.argv

class App:
	def __init__(self):
		log.info(__name__, 'Building GUI Window')
		self.mainUI = Tkinter.Tk()

		searchLabel = Tkinter.Label(self.mainUI, text="Find ID:")
		searchLabel.grid(row=0, column=0)

		# set up the file tree
		self.fileTree = ttk.Treeview(self.mainUI)
		self.fileTree.grid(row=1, column=1, columnspan=6, ipadx=150, ipady=300)
		self.fileTree.insert('', 'end', 'ACU', text='ACU')
		fileTreeScroll = ttk.Scrollbar(self.mainUI, orient="vertical", command=self.fileTree.yview)
		fileTreeScroll.grid(row=1, column=0, ipady=300)
		self.fileTree.configure(yscrollcommand=fileTreeScroll.set)

		self.fileTree.bind("<<TreeviewSelect>>", self.onClick)
		self.fileTree.bind("<Double-1>", self.onDoubleClick)

		log.info(__name__, 'Building File List')

		# fileList is a dictionary of each forge file on the first level and
		# each datafile on the second level under each forge file. This is used
		# as a cheap way to find the location a file is stored under.
		# this function also loads all the forge files and datafiles onto the TK Tree
		self.fileList = readForge(self.fileTree, CONFIG["ACUnityFolder"])

		# load all the decompressed files onto the TK Tree
		tempFiles.populateTree(self.fileTree)

		log.info(__name__, 'Finished Building File List')

		self.search = Tkinter.Entry(self.mainUI)
		self.search.grid(row=0, column=1)
		find = Tkinter.Button(self.mainUI, text='Find', command=self.searchFor)
		find.grid(row=0, column=2)

		clear = Tkinter.Button(self.mainUI, text='Clear Search', command=self.clearSearch)
		clear.grid(row=0, column=3)

		runCode = Tkinter.Button(self.mainUI, text='Run Code', command=self.runcode)
		runCode.grid(row=0, column=4)

		infobutton = Tkinter.Button(self.mainUI, text='Info', command=self.info)
		infobutton.grid(row=0, column=5)

		self.mainUI.mainloop()

	def onClick(self, event):
		fileID = self.fileTree.selection()[0]
		if len(fileID.split('|')) == 3 and len(self.fileTree.get_children(fileID)) == 0:
			decompressDatafile(self.fileTree, self.fileList, fileID.split('|')[2], fileID.split('|')[1])

	def onDoubleClick(self, event):
		fileID = self.fileTree.selection()[0]
		if len(fileID.split('|')) == 4:
			readFile(self.fileTree, self.fileList, fileID.split('|')[3])

	def searchFor(self):
		if self.search.get() != '':
			fileID = self.search.get().replace(' ', '').upper()
			readFile(self.fileTree, self.fileList, fileID)

	def clearSearch(self):
		self.search.delete(0, Tkinter.END)

	def runcode(self):
		exec self.search.get()

	def info(self, input=None):
		if self.search.get() == '' and input == None:
			return
		if self.search.get() != '':
			fileID = self.search.get().replace(' ', '').upper()
		if input != None:
			fileID = input.replace(' ', '').upper()
		if not tempFiles.exists(fileID):
			decompressDatafile(self.fileTree, self.fileList, fileID)
		if not tempFiles.exists(fileID):
			raise Exception()
		print fileID
		print tempFiles.read(fileID)


if __name__ == '__main__':
	app = App()
	with open('./config.json', 'w') as f:
		json.dump(CONFIG, f)