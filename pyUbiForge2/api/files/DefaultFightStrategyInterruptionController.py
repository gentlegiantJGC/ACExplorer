from pyUbiForge2.api.game import SubclassBaseFile
from .FightStrategyInterruptionController import FightStrategyInterruptionController as _FightStrategyInterruptionController


class DefaultFightStrategyInterruptionController(SubclassBaseFile):
    ResourceType = 0x1E468981
    ParentResourceType = _FightStrategyInterruptionController.ResourceType
    parent: _FightStrategyInterruptionController

