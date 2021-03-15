from plugins import BasePlugin
import os
from typing import Union, List
import pyUbiForge
import logging


class Plugin(BasePlugin):
    plugin_name = "Test Formatting"
    plugin_level = 3
    dev = True
    _options = [{"File Types": "0984415E;85C817C3;3F742D26"}]

    def run(
        self,
        file_id: Union[str, int],
        forge_file_name: str,
        datafile_id: int,
        options: Union[List[dict], None] = None,
    ):
        if options is not None:
            self._options = options  # should do some validation here

        file_types = [
            file_type.upper()
            for file_type in self._options[0].get("File Types", "").split(";")
        ]

        for file_id in (
            pyUbiForge.forge_files[forge_file_name].datafiles[datafile_id].files.keys()
        ):
            data = pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)
            if data is None:
                logging.warning(f"Failed to find file {file_id:016X}")
                return
            if data.file_type not in file_types:
                continue

            output = pyUbiForge.read_file(data.file)

            if output is None:
                logging.warning(data.file_name)
                out_file = open(
                    os.path.join(
                        pyUbiForge.CONFIG.get("dumpFolder", "output"),
                        f"{pyUbiForge.game_identifier()}_{data.file_name}_{file_id:016X}.format",
                    ),
                    "w",
                )
                pyUbiForge.read_file(data.file, out_file)

    def options(self, options: Union[List[dict], None]):
        if options is None or (isinstance(options, list) and len(options) == 0):
            return {
                "File Types": {
                    "type": "str_entry",
                    "default": self._options[0]["File Types"],
                }
            }
        else:
            self._options = options
