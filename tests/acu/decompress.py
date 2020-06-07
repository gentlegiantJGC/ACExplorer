import unittest
from tests import ACUPath
from pyUbiForge2.games import ACUGame


@unittest.skipIf(ACUPath is None, reason="ACU Path not defined.")
class DecompressTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._game = ACUGame(ACUPath)

    def test_decompress(self):
        for forge_file in self._game.forge_files.values():
            for data_file_id in forge_file.data_file_ids:
                forge_file.get_decompressed_files(data_file_id)


if __name__ == '__main__':
    unittest.main()
