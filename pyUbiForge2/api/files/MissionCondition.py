from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConditionBase import MissionConditionBase as _MissionConditionBase


class MissionCondition(SubclassBaseFile):
    ResourceType = 0x0E243544
    ParentResourceType = _MissionConditionBase.ResourceType
    parent: _MissionConditionBase

