"""
	This is an explorer for the forge file format used in a number of Ubisoft games mainly consisting
	of the Assassin's Creed franchise. 	This is just a UI wrapper for pyUbiForge where the heavy lifting is done.
"""

import tkinter
from tkinter import ttk, filedialog
from typing import Union
import pyUbiForge


class App:
	"""This is the class that contains all the UI features for ACExplorer.

	This class also sets up pyUbiForge.
	"""
	def __init__(self):
		self.pyUbiForge = pyUbiForge.PyUbiForgeMain()
		self.log = self.pyUbiForge.log
		self.log.info(__name__, 'Building GUI Window')

		# main UI window
		self.main_ui = tkinter.Tk()
		self.main_ui.title('ACExplorer')
		self.main_ui.iconbitmap('icon.ico')

		# set up the right click class
		self.right_click_dialogue = RightClickDialogue(self)

		# menu
		self.menu = {'main': tkinter.Menu(self.main_ui)}
		self.menu['file'] = tkinter.Menu(self.menu['main'], tearoff=0)
		self.main_ui.config(menu=self.menu['main'])
		self.menu['main'].add_cascade(label='File', menu=self.menu['file'])
		self.menu['file'].add_command(label='Options', command=self.options_dialogue)

		# set up the file tree
		self.file_tree = ttk.Treeview(self.main_ui)
		self.file_tree.grid(row=1, column=1, columnspan=4, ipadx=150, ipady=300)
		file_tree_scroll = ttk.Scrollbar(self.main_ui, orient='vertical', command=self.file_tree.yview)
		file_tree_scroll.grid(row=1, column=0, ipady=300)
		self.file_tree.configure(yscrollcommand=file_tree_scroll.set)
		self.file_tree.bind('<<TreeviewSelect>>', self.on_click)
		self.file_tree.bind('<Button-3>', self.on_right_click)

		# Load the game. This should ultimately be based on an entry in CONFIG
		self.load_game('ACU')

		# search functionality is currently commented out. Need to work out a better way to enable searching
		# search_label = tkinter.Label(self.main_ui, text='Find ID:')
		# search_label.grid(row=0, column=0)
		# self.search = tkinter.Entry(self.main_ui)
		# self.search.grid(row=0, column=1)
		# find = tkinter.Button(self.main_ui, text='Find', command=self.search_for)
		# find.grid(row=0, column=2)
		# clear = tkinter.Button(self.main_ui, text='Clear Search', command=self.clear_search)
		# clear.grid(row=0, column=3)

		# if self.dev:
		# 	test_formatting = tkinter.Button(self.main_ui, text='Test Formatting', command=self.test_formatting)
		# 	test_formatting.grid(row=0, column=51)

		self.main_ui.mainloop()

	def load_game(self, game_identifier: str):
		"""Tell pyUbiForge to load the new game and populate the file tree with the data it gives."""
		self.pyUbiForge.load_game(game_identifier)
		self.file_tree.delete(*self.file_tree.get_children())
		self.file_tree.insert('', 'end', game_identifier, text=game_identifier)

		for forge_file_name, forge_file in self.pyUbiForge.forge_files.items():
			self.file_tree.insert(game_identifier, 'end', f'{game_identifier}|{forge_file_name}', text=forge_file_name)
			for datafile_id, datafile in sorted(forge_file.datafiles.items(), key=lambda v: v[1].file_name.lower()):
				self.file_tree.insert(f'{game_identifier}|{forge_file_name}', 'end', f'{game_identifier}|{forge_file_name}|{datafile_id}', text=datafile.file_name)

	def options_dialogue(self):
		dia = OptionsDialogue(self.pyUbiForge.CONFIG)
		update = dia.update
		if update:
			self.load_game(self.pyUbiForge.game_identifier)

	def on_click(self, _):
		"""When an entry in the treeview is clicked decompress it and populate the tree"""
		line_unique_identifier = self.file_tree.selection()[0]
		if len(line_unique_identifier.split('|')) == 3 and len(self.file_tree.get_children(line_unique_identifier)) == 0:
			forge_file, datafile_id = line_unique_identifier.split('|')[1:]
			self.pyUbiForge.forge_files[forge_file].decompress_datafile(int(datafile_id))
			self.populate_tree()

	def on_right_click(self, event):
		"""Create a context menu with the possible export methods.

		When an entry in the treeview is right clicked, ask pyUbiForge.right_click_plugins for the valid plugins
		and create a context menu for the user to select from."""
		unique_identifier = self.file_tree.identify_row(event.y)
		if unique_identifier:
			self.file_tree.selection_set(unique_identifier)
			unique_identifier = unique_identifier.split('|')
			forge_file_name = datafile_id = None
			if len(unique_identifier) >= 2:
				forge_file_name = unique_identifier[1]
			if len(unique_identifier) >= 3:
				datafile_id = int(unique_identifier[2])
			plugin_names, file_id = self.pyUbiForge.right_click_plugins.query(len(unique_identifier), unique_identifier[-1], forge_file_name, datafile_id)
			self.right_click_dialogue.post(event, plugin_names, file_id, forge_file_name, datafile_id)
		else:
			pass

	def populate_tree(self):
		"""A helper function to populate files in the treeview."""
		game_identifier = self.pyUbiForge.game_identifier
		for forge_file_name, forge_file in self.pyUbiForge.forge_files.items():
			for datafile_id in forge_file.new_datafiles:
				for file_id, file_name in sorted(forge_file.datafiles[datafile_id].files.items(), key=lambda v: v[1].lower()):
					self.file_tree.insert(
						f'{game_identifier}|{forge_file_name}|{datafile_id}', 'end',
						f'{self.pyUbiForge.game_identifier}|{forge_file_name}|{datafile_id}|{file_id}',
						text=file_name
					)
			forge_file.new_datafiles.clear()

	# def search_for(self):
	# 	search = self.search.get()
	# 	if search != '':
	# 		if ',' in search:
	# 			for file_id in search.split(','):
	# 				file_id = file_id.replace(' ', '').upper()
	# 				self.game_functions.read_file(self, file_id)
	# 		else:
	# 			file_id = self.search.get().replace(' ', '').upper()
	# 			self.game_functions.read_file(self, file_id)

	# def clear_search(self):
	# 	self.search.delete(0, tkinter.END)

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
	# 	# 			self.game_functions.formatFile.topLevelFormat(self, fileID)
	# 	# 			count -= 1
	# 	# 			if count == 0:
	# 	# 				break
	# 	# TODO


class OptionsDialogue:
	"""A separate UI where the CONFIG options can be changed."""
	# TODO make it so that the main program pauses when this is open and multiple can't be opened.
	def __init__(self, CONFIG: pyUbiForge.misc.Config):
		self.CONFIG = CONFIG
		self.main_ui = tkinter.Toplevel()
		self.main_ui.title('ACExplorer Options')
		self._update = False

		# options
		self.game_paths = {}

		self.dump_folder = self.folder_option('Dump Folder', self.CONFIG['dumpFolder'], 0)

		row = 1
		for game_identifier, location in self.CONFIG['gameFolders'].items():
			self.game_paths[game_identifier] = self.folder_option(f'{game_identifier} Folder', location, row)
			row += 1

		# save and quit buttons
		self.buttons = tkinter.Frame(self.main_ui)
		self.buttons.grid(row=1000, column=0, columnspan=3)
		self.save_button = tkinter.Button(self.buttons, text='OK', command=self.save)
		self.save_button.grid(row=0, column=0)
		self.quitButton = tkinter.Button(self.buttons, text='Quit', command=self.quit)
		self.quitButton.grid(row=0, column=1)

	def folder_option(self, desc: str, val: str, row: int) -> tkinter.Label:
		"""A helper function to add folder selectors for each game."""
		desc_label = tkinter.Label(self.main_ui, text=desc)
		desc_label.grid(row=row, column=0)
		path_label = tkinter.Label(self.main_ui, text=val)
		path_label.grid(row=row, column=1)
		browse_button = tkinter.Button(self.main_ui, text='Browse', command=lambda: self.browse(path_label))
		browse_button.grid(row=row, column=2)
		return path_label

	def quit(self):
		"""Quit without saving."""
		self.main_ui.destroy()

	def save(self):
		"""Save the inputs back to CONFIG and close."""
		for game_identifier, label in self.game_paths.items():
			self.CONFIG['gameFolders'][game_identifier] = label['text']
		self.CONFIG['dumpFolder'] = self.dump_folder['text']
		self._update = True
		self.main_ui.destroy()

	@staticmethod
	def browse(value_to_set: tkinter.Label):
		"""When a folder is selected update the text next to it to reflect the folder chosen."""
		folder_path = filedialog.askdirectory()
		if folder_path != '':
			value_to_set.config(text=folder_path)

	@property
	def update(self):
		"""After initiating this class call this method.

		This method will wait until the window has been destroyed and then
		return True if the save method was called or False otherwise."""
		self.main_ui.wait_window()
		return self._update


class RightClickDialogue:
	"""The right click context menu UI that shows which export methods can be used."""
	def __init__(self, app_: App):
		self.app = app_
		self.menu = tkinter.Menu(self.app.main_ui, tearoff=0)

	def post(self, event, plugin_names: list, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None):
		"""Call to populate and show the context menu"""
		self.menu.delete(0, tkinter.END)
		if len(plugin_names) > 0:
			for plugin_name in plugin_names:
				self.add_command(plugin_name, file_id, forge_file_name, datafile_id)

			try:
				self.menu.tk_popup(event.x_root, event.y_root)
			finally:
				self.menu.grab_release()

	def add_command(self, plugin_name, file_id: Union[str, int], forge_file_name: Union[None, str] = None, datafile_id: Union[None, int] = None):
		"""Workaround for plugin in post method getting overwritten which lead to all options calling the last plugin."""
		self.menu.add_command(
			label=plugin_name,
			command=lambda: self.run_plugin(plugin_name, file_id, forge_file_name, datafile_id)
		)

	def run_plugin(self, plugin_name, file_id, forge_file_name, datafile_id):
		options = []
		while options is not None:
			options, output = self.app.pyUbiForge.right_click_plugins.run(plugin_name, file_id, forge_file_name, datafile_id, options)
			# TODO: show options screen, wait for response from option screen


if __name__ == '__main__':
	app = App()
	app.pyUbiForge.save()
