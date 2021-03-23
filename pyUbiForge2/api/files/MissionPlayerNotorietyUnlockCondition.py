from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionPlayerNotorietyUnlockCondition(SubclassBaseFile):
    ResourceType = 0xCA5E2033
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

