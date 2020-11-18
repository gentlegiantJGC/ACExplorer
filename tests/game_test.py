import time
import unittest
from typing import Type
from pyUbiForge2.api import log, BaseGame


class BaseGameTestCase:
    class BaseGameTestCase(unittest.TestCase):
        @classmethod
        def setUpGame(cls, game_class: Type[BaseGame], game_path: str):
            cls._game = game_class(game_path)
            return cls

        def test_decompress(self):
            start_time = time.time()
            for forge_file in self._game.forge_files.values():
                for data_file_id in forge_file.data_file_ids:
                    forge_file.get_decompressed_files(data_file_id)
                log.info(f"Finished decompressing {forge_file.file_name}")
            log.info(f"Finished decompressing all forge files in {round(time.time()-start_time)} seconds")
