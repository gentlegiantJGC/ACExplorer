"""
	This is an explorer for the forge file format used in Assassin's Creed
	The format varies slightly between games and the current implementation will only work
	with Assassin's Creed Unity.
	The forge file format is similar to a zip file in concept however each individual containing
	file can be decompressed individually.
	The 'folders' in the top level of the forge file will from this point on be referred to as datafiles.
	Contained within the datafiles are a variety of files related to that datafile.
"""

import json
import ttk
import Tkinter
import tkFileDialog
import sys
import os
import ACExplorer


class App:
	def __init__(self):
		self.CONFIG = ACExplorer.CONFIG
		self.dev = 'dev' in sys.argv
		self.misc = ACExplorer.misc
		self.gameFunctions = None
		self.log = self.misc.Logger(self)
		self.tempNewFiles = self.misc.tempFilesContainer(self)
		self.log.info(__name__, 'Building GUI Window')
		self.main_ui = Tkinter.Tk()
		self.main_ui.title('ACExplorer')

		# menu
		self.menu = {
			'main': Tkinter.Menu(self.main_ui)
		}
		self.menu['file'] = Tkinter.Menu(self.menu['main'])
		self.main_ui.config(menu=self.menu['main'])
		self.menu['main'].add_cascade(label='File', menu=self.menu['file'])
		self.menu['file'].add_command(label='Options', command=self.options_dialogue)

		search_label = Tkinter.Label(self.main_ui, text='Find ID:')
		search_label.grid(row=0, column=0)

		# set up the file tree
		self.file_tree = ttk.Treeview(self.main_ui)
		self.file_tree.grid(row=1, column=1, columnspan=4, ipadx=150, ipady=300)
		file_tree_scroll = ttk.Scrollbar(self.main_ui, orient='vertical', command=self.file_tree.yview)
		file_tree_scroll.grid(row=1, column=0, ipady=300)
		self.file_tree.configure(yscrollcommand=file_tree_scroll.set)

		self.file_tree.bind('<<TreeviewSelect>>', self.on_click)
		self.file_tree.bind('<Button-3>', self.right_click)
		self.file_tree.bind('<Double-1>', self.on_double_click)

		self.log.info(__name__, 'Building File List')

		# file_list is a dictionary of each forge file on the first level and
		# each datafile on the second level under each forge file. This is used
		# as a cheap way to find the location a file is stored under.
		# this function also loads all the forge files and datafiles onto the TK Tree
		self.file_list = {}

		self.load_game('ACU')

		self.log.info(__name__, 'Finished Building File List')

		self.search = Tkinter.Entry(self.main_ui)
		self.search.grid(row=0, column=1)
		find = Tkinter.Button(self.main_ui, text='Find', command=self.search_for)
		find.grid(row=0, column=2)

		clear = Tkinter.Button(self.main_ui, text='Clear Search', command=self.clear_search)
		clear.grid(row=0, column=3)

		if self.dev:
			run_code = Tkinter.Button(self.main_ui, text='Run Code', command=self.runcode)
			run_code.grid(row=0, column=50)

			# test_formatting = Tkinter.Button(self.main_ui, text='Test Formatting', command=self.test_formatting)
			# test_formatting.grid(row=0, column=51)

		self.main_ui.mainloop()

	def load_game(self, game_identifier):
		if self.gameFunctions is not None and self.tempNewFiles.lightDictChanged:
			with open('./resources/lightDict/{}.json'.format(self.gameFunctions.gameIdentifier), 'w') as light_dict:
				json.dump(self.tempNewFiles.lightDictionary, light_dict)
		self.tempNewFiles.clear()
		self.file_tree.delete(*self.file_tree.get_children())
		if game_identifier in ACExplorer.games:
			self.gameFunctions = ACExplorer.games[game_identifier]
			self.file_list = self.gameFunctions.framework.read_forge(self, self.CONFIG.game_folder(game_identifier))
			# load all the decompressed files onto the TK Tree

			if os.path.isdir('./resources/lightDict/{}.json'.format(self.gameFunctions.gameIdentifier)):
				with open('./resources/lightDict/{}.json'.format(self.gameFunctions.gameIdentifier), 'r') as light_dict:
					self.tempNewFiles.lightDictionary = json.load(light_dict)

	def options_dialogue(self):
		dia = OptionsDialogue(self.CONFIG)
		update = dia.update
		if update:
			self.load_game(self.gameFunctions.gameIdentifier)

	def on_click(self, _):
		line_unique_identifier = self.file_tree.selection()[0]
		if len(line_unique_identifier.split('|')) == 3 and len(self.file_tree.get_children(line_unique_identifier)) == 0:
			self.gameFunctions.framework.decompress_datafile(self, int(line_unique_identifier.split('|')[2]), line_unique_identifier.split('|')[1])

	def right_click(self, event):
		line_unique_identifier = self.file_tree.identify_row(event.y)
		if line_unique_identifier:
			self.file_tree.selection_set(line_unique_identifier)
			depth = line_unique_identifier.split('|')

			# self.contextMenu.post(event.x_root, event.y_root)
		else:
			pass

	def on_double_click(self, _):
		line_unique_identifier = self.file_tree.selection()[0]
		if len(line_unique_identifier.split('|')) == 4:
			self.gameFunctions.read_file(self, int(line_unique_identifier.split('|')[3]), line_unique_identifier.split('|')[1], int(line_unique_identifier.split('|')[2]))

	def search_for(self):
		search = self.search.get()
		if search != '':
			if ',' in search:
				for file_id in search.split(','):
					file_id = file_id.replace(' ', '').upper()
					self.gameFunctions.read_file(self, file_id)
			else:
				file_id = self.search.get().replace(' ', '').upper()
				self.gameFunctions.read_file(self, file_id)

	def clear_search(self):
		self.search.delete(0, Tkinter.END)

	def runcode(self):
		exec self.search.get()

	# def test_formatting(self):
	# 	file_type = self.search.get()
	# 	count = 0
	# 	if ':' in file_type:
	# 		file_type, count = file_type.split(':')[:2]
	# 		try:
	# 			count = int(count)
	# 		except Exception as e:
	# 			raise Exception('Need numerical value got "{}"\n{}'.format(count, e))
	# 	file_type = file_type.upper()
	# 	# if len(fileType) == 8:
	# 	# 	for fileID in tempFiles.tempFileContainer.keys():
	# 	# 		if tempFiles.tempFileContainer[fileID][0]['fileType'] in [fileType, ''.join([fileType[a:a+2] for a in [6,4,2,0]])]:
	# 	# 			self.gameFunctions.formatFile.topLevelFormat(self, fileID)
	# 	# 			count -= 1
	# 	# 			if count == 0:
	# 	# 				break
	# 	# TODO


class OptionsDialogue:
	def __init__(self, CONFIG):
		self.CONFIG = CONFIG
		self.main_ui = Tkinter.Toplevel()
		self.main_ui.title('ACExplorer Options')
		self._update = False

		# options
		self.game_paths = {}

		row = 0
		self.dump_folder = self.folder_option('Dump Folder', self.CONFIG['dumpFolder'], row)

		row += 1
		for game_identifier, location in self.CONFIG['gameFolders'].iteritems():
			self.game_paths[game_identifier] = self.folder_option('{} Folder'.format(game_identifier), location, row)
			row += 1

		# save and quit buttons
		self.buttons = Tkinter.Frame(self.main_ui)
		self.buttons.grid(row=1000, column=0, columnspan=3)
		self.save_button = Tkinter.Button(self.buttons, text='OK', command=self.save)
		self.save_button.grid(row=0, column=0)
		self.quitButton = Tkinter.Button(self.buttons, text='Quit', command=self.quit)
		self.quitButton.grid(row=0, column=1)

	def folder_option(self, desc, val, row):
		desc_label = Tkinter.Label(self.main_ui, text=desc)
		desc_label.grid(row=row, column=0)
		path_label = Tkinter.Label(self.main_ui, text=val)
		path_label.grid(row=row, column=1)
		browse_button = Tkinter.Button(self.main_ui, text='Browse', command=lambda: self.browse(path_label))
		browse_button.grid(row=row, column=2)
		return path_label

	def quit(self):
		self.main_ui.destroy()

	def save(self):
		for game_identifier, label in self.game_paths.iteritems():
			self.CONFIG['gameFolders'][game_identifier] = label['text']
		self.CONFIG['dumpFolder'] = self.dump_folder['text']
		self._update = True
		self.main_ui.destroy()

	@staticmethod
	def browse(value_to_set):
		folder_path = tkFileDialog.askdirectory()
		if folder_path != '':
			value_to_set.config(text=folder_path)

	@property
	def update(self):
		self.main_ui.wait_window()
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
