import unittest
from tests.game_test import BaseGameTestCase
from tests import AC2BMPPath as GamePath
from pyUbiForge2.games import AC2BMPGame as Game


@unittest.skipIf(GamePath is None, reason=f"{Game.GameIdentifier} Path not defined.")
class AC2BMPTestCase(BaseGameTestCase.BaseGameTestCase):
    @classmethod
    def setUpClass(cls):
        return cls.setUpGame(Game, GamePath)


if __name__ == "__main__":
    unittest.main()
