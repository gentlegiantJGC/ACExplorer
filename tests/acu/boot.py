import unittest
import time

from tests.acu import GamePath, Game
from pyUbiForge2.api import log


@unittest.skipIf(GamePath is None, reason=f"{Game.GameIdentifier} Path not defined.")
class BootTestCase(unittest.TestCase):
    @staticmethod
    def test_decompress():
        start_time = time.time()
        Game(GamePath)
        log.info(f"Finished decompressing all forge files in {round(time.time()-start_time)} seconds")


if __name__ == '__main__':
    unittest.main()
