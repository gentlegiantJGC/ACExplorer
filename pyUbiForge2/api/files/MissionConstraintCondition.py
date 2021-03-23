from pyUbiForge2.api.game import SubclassBaseFile
from .MissionConditionBase import MissionConditionBase as _MissionConditionBase


class MissionConstraintCondition(SubclassBaseFile):
    ResourceType = 0xF5BC70FF
    ParentResourceType = _MissionConditionBase.ResourceType
    parent: _MissionConditionBase
