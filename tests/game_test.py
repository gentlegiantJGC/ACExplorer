import time
import unittest
from typing import Type
import os

from pyUbiForge2.api import log, BaseGame


class BaseGameTestCase:
    class BaseGameTestCase(unittest.TestCase):
        @classmethod
        def setUpGame(cls, game_class: Type[BaseGame], game_path: str):
            cls._game = game_class(game_path)
            return cls

        def test_setup(self):
            pass

        def _test_file(self, resource_type: int):
            failures = 0
            success = 0
            for forge_name, forge_file in self._game.forge_files.items():
                for data_file_id, data_file in forge_file.data_files.items():
                    for file_id, (resource_type_, file_name) in data_file.files.items():
                        if resource_type == resource_type_:
                            try:
                                self._game.get_file(file_id, forge_name, data_file_id)
                                success += 1
                            except:
                                failures += 1
                                sane_file_name = "".join([c for c in file_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                                path = f"./error_format/{self._game.GameIdentifier}/{forge_name}/{data_file_id:X}/{file_id:X}{sane_file_name}.bin"
                                os.makedirs(os.path.dirname(path), exist_ok=True)
                                try:
                                    self._game.get_file(file_id, forge_name, data_file_id, path)
                                except:
                                    pass
                                if failures >= 100:
                                    raise Exception(f"Success {success}, Failure {failures}")
            print(f"Success {success}, Failure {failures}")

        def test_mesh(self):
            self._test_file(0x415D9568)

        @unittest.skip
        def test_decompress(self):
            start_time = time.time()
            for forge_file in self._game.forge_files.values():
                for data_file_id in forge_file.data_file_ids:
                    forge_file.get_decompressed_files(data_file_id)
                log.info(f"Finished decompressing {forge_file.file_name}")
            log.info(f"Finished decompressing all forge files in {round(time.time()-start_time)} seconds")
