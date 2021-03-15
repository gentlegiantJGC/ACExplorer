import os
from plugins import BasePlugin
from typing import Union, List
import pyUbiForge
import logging


class Plugin(BasePlugin):
    plugin_name = "Format"
    plugin_level = 4
    file_type = "*"

    def run(
        self,
        file_id: Union[str, int],
        forge_file_name: str,
        datafile_id: int,
        options: Union[List[dict], None] = None,
    ):
        data = pyUbiForge.temp_files(file_id, forge_file_name, datafile_id)
        if data is None:
            logging.warning(f"Failed to find file {file_id:016X}")
            return
        if not os.path.isdir(pyUbiForge.CONFIG.get("dumpFolder", "output")):
            os.makedirs(pyUbiForge.CONFIG.get("dumpFolder", "output"))
        out_file = open(
            os.path.join(
                pyUbiForge.CONFIG.get("dumpFolder", "output"),
                f"{pyUbiForge.game_identifier()}_{data.file_name}_{file_id:016X}.format",
            ),
            "w",
        )
        pyUbiForge.read_file(data.file, out_file)
        logging.info("Finished Formatting")
