import unittest
import os
import traceback

from pyUbiForge2.api import log
from tests.acu import GamePath, Game
from pyUbiForge2.api.data_types import FileResourceType

FormatFile = False


@unittest.skipIf(GamePath is None, reason=f"{Game.GameIdentifier} Path not defined.")
class ReadTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._game = Game(GamePath)

    def _read_file(self, resource_id: FileResourceType, max_count=100, start_count=0):
        count = 0
        success = 0
        fail = 0

        def save_file_bytes():
            with open(path, "wb") as f:
                f.write(
                    self._game.get_file_bytes(file_id, forge_file_name, data_file_id)
                )

        for forge_file_name, forge_file in self._game.forge_files.items():
            for data_file_id, data_file in forge_file.data_files.items():
                for file_id, (resource_id_, file_name) in data_file.files.items():
                    if resource_id == resource_id_:
                        if count < start_count:
                            count += 1
                            continue
                        log.info(
                            f"{forge_file_name}, {data_file_id}, {file_id}-{file_name}"
                        )
                        path = os.path.join(
                            "temp", f"{resource_id:08X}", forge_file_name, file_name
                        )
                        os.makedirs(os.path.dirname(path), exist_ok=True)
                        if FormatFile:
                            save_file_bytes()

                        try:
                            if FormatFile:
                                self._game.get_file(
                                    file_id,
                                    forge_file_name,
                                    data_file_id,
                                    path + ".format",
                                )
                            else:
                                self._game.get_file(file_id, forge_file_name)
                            success += 1
                        except Exception as e:
                            log.error(f"{file_name}: {e}")
                            traceback.print_exc()
                            save_file_bytes()
                            if not FormatFile:
                                try:
                                    self._game.get_file(
                                        file_id,
                                        forge_file_name,
                                        data_file_id,
                                        path + ".format",
                                    )
                                except:
                                    pass
                            fail += 1
                        count += 1
                        if count >= max_count:
                            log.info(
                                f"{100*success/max_count}% succeeded, {100*fail/max_count}% failed"
                            )
                            return

    def test_mesh(self):
        self._read_file(int("415D9568", 16))

    def test_entity(self):
        self._read_file(int("0984415E", 16), 10000)

    def test_level_main(self):
        self._read_file(int("FBB63E47", 16), 1, 15)

    def test_skeleton(self):
        self._read_file(int("24AECB7C", 16), 300)


if __name__ == "__main__":
    unittest.main()
