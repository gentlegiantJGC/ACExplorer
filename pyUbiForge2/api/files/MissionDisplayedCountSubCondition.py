from pyUbiForge2.api.game import SubclassBaseFile
from .MissionMaxCountSubCondition import (
    MissionMaxCountSubCondition as _MissionMaxCountSubCondition,
)


class MissionDisplayedCountSubCondition(SubclassBaseFile):
    ResourceType = 0x29A27A62
    ParentResourceType = _MissionMaxCountSubCondition.ResourceType
    parent: _MissionMaxCountSubCondition
