import unittest
from tests.game_test import BaseGameTestCase
from tests import AC3LPath as GamePath
from pyUbiForge2.games import AC3LGame as Game


@unittest.skipIf(GamePath is None, reason=f"{Game.GameIdentifier} Path not defined.")
class AC3LTestCase(BaseGameTestCase.BaseGameTestCase):
    @classmethod
    def setUpClass(cls):
        return cls.setUpGame(Game, GamePath)


if __name__ == '__main__':
    unittest.main()
