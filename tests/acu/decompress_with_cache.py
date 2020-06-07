import unittest
import time

from tests import ACUPath
from pyUbiForge2.games import ACUGame
from pyUbiForge2.api import log


@unittest.skipIf(ACUPath is None, reason="ACU Path not defined.")
class DecompressWithCacheTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._game = ACUGame(ACUPath)

    def test_decompress(self):
        start_time = time.time()
        for forge_file_name, forge_file in self._game.forge_files.items():
            for data_file_id in forge_file.data_file_ids:
                self._game.get_file_bytes(data_file_id, forge_file_name, data_file_id)
            log.info(f"Finished decompressing {forge_file.file_name}")
        log.info(f"Finished decompressing all forge files in {round(time.time()-start_time)} seconds")


if __name__ == '__main__':
    unittest.main()
