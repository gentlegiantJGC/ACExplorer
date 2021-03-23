from pyUbiForge2.api.game import SubclassBaseFile
from .MissionCondition import MissionCondition as _MissionCondition


class MissionConditionDLC(SubclassBaseFile):
    ResourceType = 0xD26AEF58
    ParentResourceType = _MissionCondition.ResourceType
    parent: _MissionCondition

