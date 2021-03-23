from pyUbiForge2.api.game import SubclassBaseFile
from .MissionMaxTimeSubCondition import MissionMaxTimeSubCondition as _MissionMaxTimeSubCondition


class MissionDiplayedTimeSubCondition(SubclassBaseFile):
    ResourceType = 0x6B811348
    ParentResourceType = _MissionMaxTimeSubCondition.ResourceType
    parent: _MissionMaxTimeSubCondition

