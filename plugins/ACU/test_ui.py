from pyUbiForge.misc.plugins import BasePlugin
from typing import Union, List
import logging


class Plugin(BasePlugin):
	plugin_name = 'Test UI'
	plugin_level = 1
	dev = True
	_options = []

	def run(self, *_):
		logging.info(self._options)

	def options(self, options: Union[List[dict], None]):
		if options is None or (isinstance(options, list) and len(options) == 0):
			return {
				"Select": {
					"type": "select",
					"options": [
						"Option 1",
						"Option 2"
					]
				},
				"Str Entry": {
					"type": "str_entry",
					"default": "Hello World!"
				},
				"Int Entry": {
					"type": "int_entry",
					"default": 0
				},
				"Int Entry (-50 to 50)": {
					"type": "int_entry",
					"default": 0,
					"min": -50,
					"max": 50
				},
				"Float Entry": {
					"type": "float_entry",
					"default": 0
				},
				"Float Entry (e to pi)": {
					"type": "float_entry",
					"default": 0,
					"min": 2.7182818284,
					"max": 3.1415926536
				},
				"Checkbox": {
					"type": "check_box",
					"default": True
				},
				"Directory Select": {
					"type": "dir_select"
				},
				"File Select": {
					"type": "file_select"
				}
			}

		else:
			self._options = options
