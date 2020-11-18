import unittest
from tests.game_test import BaseGameTestCase
from tests import ACUPath as GamePath
from pyUbiForge2.games import ACUGame as Game


@unittest.skipIf(GamePath is None, reason=f"{Game.GameIdentifier} Path not defined.")
class ACUTestCase(BaseGameTestCase.BaseGameTestCase):
    @classmethod
    def setUpClass(cls):
        return cls.setUpGame(Game, GamePath)

    def test_decompress(self):
        super().test_decompress()


if __name__ == '__main__':
    unittest.main()
