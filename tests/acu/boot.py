import unittest
import time

from tests import ACUPath
from pyUbiForge2.games import ACUGame
from pyUbiForge2.api import log


@unittest.skipIf(ACUPath is None, reason="ACU Path not defined.")
class BootTestCase(unittest.TestCase):
    @staticmethod
    def test_decompress():
        start_time = time.time()
        ACUGame(ACUPath)
        log.info(f"Finished decompressing all forge files in {round(time.time()-start_time)} seconds")


if __name__ == '__main__':
    unittest.main()
