'''
	This is an explorer for the forge file format used in Assassin's Creed
	The format varies slightly between games and the current implementation will only work
	with Assassin's Creed Unity.
	The forge file format is similar to a zip file in concept however each individual containing
	file can be decompressed individually.
	The 'folders' in the top level of the forge file will from this point on be referred to as datafiles.
	Contained within the datafiles are a variety of files related to that datafile.
'''

import json
import ttk
import Tkinter
import tkFileDialog
import sys
import os
from ACExplorer import misc, CONFIG, ACUnity

class App:
	def __init__(self):
		self.CONFIG = CONFIG
		self.dev = 'dev' in sys.argv
		self.misc = misc
		self.gameFunctions = ACUnity
		self.log = self.misc.logger(self)
		self.tempNewFiles = self.misc.tempFilesContainer(self)
		self.log.info(__name__, 'Building GUI Window')
		self.mainUI = Tkinter.Tk()
		self.mainUI.title("ACExplorer")

		# menu
		self.menu = {}
		self.menu["main"] = Tkinter.Menu(self.mainUI)
		self.mainUI.config(menu=self.menu["main"])
		self.menu["file"] = Tkinter.Menu(self.menu["main"])
		self.menu["main"].add_cascade(label="File", menu=self.menu["file"])
		self.menu["file"].add_command(label="Options", command=self.optionsDialogue)

		searchLabel = Tkinter.Label(self.mainUI, text="Find ID:")
		searchLabel.grid(row=0, column=0)

		# set up the file tree
		self.fileTree = ttk.Treeview(self.mainUI)
		self.fileTree.grid(row=1, column=1, columnspan=4, ipadx=150, ipady=300)
		fileTreeScroll = ttk.Scrollbar(self.mainUI, orient="vertical", command=self.fileTree.yview)
		fileTreeScroll.grid(row=1, column=0, ipady=300)
		self.fileTree.configure(yscrollcommand=fileTreeScroll.set)

		self.fileTree.bind("<<TreeviewSelect>>", self.onClick)
		self.fileTree.bind("<Double-1>", self.onDoubleClick)

		self.log.info(__name__, 'Building File List')

		# fileList is a dictionary of each forge file on the first level and
		# each datafile on the second level under each forge file. This is used
		# as a cheap way to find the location a file is stored under.
		# this function also loads all the forge files and datafiles onto the TK Tree
		self.fileList = {}

		self.loadGame('ACU')

		self.log.info(__name__, 'Finished Building File List')

		self.search = Tkinter.Entry(self.mainUI)
		self.search.grid(row=0, column=1)
		find = Tkinter.Button(self.mainUI, text='Find', command=self.searchFor)
		find.grid(row=0, column=2)

		clear = Tkinter.Button(self.mainUI, text='Clear Search', command=self.clearSearch)
		clear.grid(row=0, column=3)

		# infobutton = Tkinter.Button(self.mainUI, text='Info', command=self.info)
		# infobutton.grid(row=0, column=4)

		if self.dev:
			runCode = Tkinter.Button(self.mainUI, text='Run Code', command=self.runcode)
			runCode.grid(row=0, column=50)

			testFormatting = Tkinter.Button(self.mainUI, text='Test Formatting', command=self.testFormatting)
			testFormatting.grid(row=0, column=51)

		self.mainUI.mainloop()

	def loadGame(self, gameIdentifier):
		if self.tempNewFiles.lightDictChanged:
			with open('./resources/lightDict/{}.json'.format(self.gameFunctions.gameIdentifier), 'w') as f:
				json.dump(self.tempNewFiles.lightDictionary, f)
		self.tempNewFiles.clear()
		self.fileTree.delete(*self.fileTree.get_children())
		if gameIdentifier == 'ACU':
			self.gameFunctions = ACUnity
			self.fileTree.insert('', 'end', 'ACU', text='ACU')
			self.fileList = self.gameFunctions.read_forge(self, self.CONFIG.gameFolder(gameIdentifier))
			# load all the decompressed files onto the TK Tree

		if os.path.isdir('./resources/lightDict/{}.json'.format(self.gameFunctions.gameIdentifier)):
			with open('./resources/lightDict/{}.json'.format(self.gameFunctions.gameIdentifier), 'r') as f:
				self.tempNewFiles.lightDictionary = json.load(f)

	def optionsDialogue(self):
		dia = OptionsDialogue(self.CONFIG)
		update = dia.update
		if update:
			self.loadGame(self.gameFunctions.gameIdentifier)


	def onClick(self, event):
		fileID = self.fileTree.selection()[0]
		if len(fileID.split('|')) == 3 and len(self.fileTree.get_children(fileID)) == 0:
			self.gameFunctions.decompressDatafile(self, int(fileID.split('|')[2]), fileID.split('|')[1])

	def onDoubleClick(self, event):
		fileID = self.fileTree.selection()[0]
		if len(fileID.split('|')) == 4:
			self.gameFunctions.readFile(self, int(fileID.split('|')[3]), fileID.split('|')[1], int(fileID.split('|')[2]))

	def searchFor(self):
		search = self.search.get()
		if search != '':
			if ',' in search:
				for fileID in search.split(','):
					fileID = fileID.replace(' ', '').upper()
					self.gameFunctions.readFile(self, fileID)
			else:
				fileID = self.search.get().replace(' ', '').upper()
				self.gameFunctions.readFile(self, fileID)

	def clearSearch(self):
		self.search.delete(0, Tkinter.END)

	# def info(self, input=None):
	# 	if self.search.get() == '' and input == None:
	# 		return
	# 	if self.search.get() != '':
	# 		fileID = self.search.get().replace(' ', '').upper()
	# 	if input != None:
	# 		fileID = input.replace(' ', '').upper()
	# 	if not tempFiles.exists(fileID):
	# 		self.gameFunctions.decompressDatafile(self, fileID)
	# 	if not tempFiles.exists(fileID):
	# 		raise Exception()
	# 	print fileID
	# 	print tempFiles.read(fileID)

	def runcode(self):
		exec self.search.get()

	def testFormatting(self):
		fileType = self.search.get()
		count = 0
		if ':' in fileType:
			fileType, count = fileType.split(':')[:2]
			try:
				count = int(count)
			except:
				raise Exception('Need numerical value got "{}"'.format(count))
		fileType = fileType.upper()
		# if len(fileType) == 8:
		# 	for fileID in tempFiles.tempFileContainer.keys():
		# 		if tempFiles.tempFileContainer[fileID][0]["fileType"] in [fileType, ''.join([fileType[a:a+2] for a in [6,4,2,0]])]:
		# 			self.gameFunctions.formatFile.topLevelFormat(self, fileID)
		# 			count -= 1
		# 			if count == 0:
		# 				break
		# TODO

class OptionsDialogue:
	def __init__(self, CONFIG):
		self.CONFIG = CONFIG
		self.mainUI = Tkinter.Toplevel()
		self.mainUI.title("ACExplorer Options")
		self._update = False

		# options
		self.game_paths = {}

		def folder_option(mainUI, desc, val, row):
			desc_label = Tkinter.Label(mainUI, text=desc)
			desc_label.grid(row=row, column=0)
			path_label = Tkinter.Label(mainUI, text=val)
			path_label.grid(row=row, column=1)
			browse_button = Tkinter.Button(mainUI, text="Browse", command=lambda: self.browse(path_label))
			browse_button.grid(row=row, column=2)
			return path_label

		row = 0
		self.dump_folder = folder_option(self.mainUI, "Dump Folder", self.CONFIG["dumpFolder"], row)

		row += 1
		for game_identifier, location in self.CONFIG["gameFolders"].iteritems():
			self.game_paths[game_identifier] = folder_option(self.mainUI, '{} Folder'.format(game_identifier), location, row)
			row += 1



		# save and quit buttons
		self.buttons = Tkinter.Frame(self.mainUI)
		self.buttons.grid(row=1000, column=0, columnspan=3)
		self.save_button = Tkinter.Button(self.buttons, text="OK", command=self.save)
		self.save_button.grid(row=0, column=0)
		self.quitButton = Tkinter.Button(self.buttons, text="Quit", command=self.quit)
		self.quitButton.grid(row=0, column=1)

	def quit(self):
		self.mainUI.destroy()

	def save(self):
		for game_identifier, label in self.game_paths.iteritems():
			self.CONFIG["gameFolders"][game_identifier] = label["text"]
		self.CONFIG["dumpFolder"] = self.dump_folder["text"]
		self._update = True
		self.mainUI.destroy()

	def browse(self, value_to_set):
		folder_path = tkFileDialog.askdirectory()
		if folder_path != '':
			value_to_set.config(text=folder_path)

	@property
	def update(self):
		self.mainUI.wait_window()
		return self._update


if __name__ == '__main__':
	app = App()
	with open('./config.json', 'w') as f:
		json.dump(app.CONFIG.raw, f, indent=4)
	if app.tempNewFiles.lightDictChanged:
		if not os.path.isdir('./resources/lightDict'):
			os.makedirs('./resources/lightDict')
		with open('./resources/lightDict/{}.json'.format(app.gameFunctions.gameIdentifier), 'w') as f:
			json.dump(app.tempNewFiles.lightDictionary, f)
