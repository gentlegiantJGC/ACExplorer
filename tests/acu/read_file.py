import unittest
import os

from pyUbiForge2.api import log
from tests.acu import GamePath, Game
from pyUbiForge2.api.data_types import FileResourceType

FormatFile = False


@unittest.skipIf(GamePath is None, reason=f"{Game.GameIdentifier} Path not defined.")
class ReadTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game(GamePath)

    def _read_file(self, resource_id: FileResourceType, max_count=100):
        count = 0
        success = 0
        fail = 0
        for forge_file_name, forge_file in self._game.forge_files.items():
            for data_file_id, data_file in forge_file.data_files.items():
                for file_id, (resource_id_, file_name) in data_file.files.items():
                    if resource_id == resource_id_:
                        path = os.path.join("temp", f"{resource_id:08X}", file_name)
                        os.makedirs(os.path.dirname(path), exist_ok=True)
                        file = self._game.get_file_bytes(file_id, forge_file_name, data_file_id)
                        if FormatFile:
                            with open(path, 'wb') as f:
                                f.write(file)
                        try:
                            if FormatFile:
                                self._game.get_file(file_id, forge_file_name, data_file_id, path + ".format")
                            else:
                                self._game.get_file(file_id, forge_file_name)
                            success += 1
                        except Exception as e:
                            log.error(f"{file_name}: {e}")
                            import traceback
                            traceback.print_exc()
                            fail += 1
                        count += 1
                        if count > max_count:
                            log.info(f"{100*success/max_count}% succeeded, {100*fail/max_count}% failed")
                            return

    def test_mesh(self):
        self._read_file(int("415D9568", 16))


if __name__ == '__main__':
    unittest.main()
