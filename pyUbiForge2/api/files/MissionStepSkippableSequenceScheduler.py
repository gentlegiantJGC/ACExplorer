from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepScheduler import MissionStepScheduler as _MissionStepScheduler


class MissionStepSkippableSequenceScheduler(SubclassBaseFile):
    ResourceType = 0xB376A68E
    ParentResourceType = _MissionStepScheduler.ResourceType
    parent: _MissionStepScheduler
