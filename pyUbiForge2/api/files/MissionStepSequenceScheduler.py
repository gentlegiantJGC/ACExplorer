from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepScheduler import MissionStepScheduler as _MissionStepScheduler


class MissionStepSequenceScheduler(SubclassBaseFile):
    ResourceType = 0x0F3CCC46
    ParentResourceType = _MissionStepScheduler.ResourceType
    parent: _MissionStepScheduler

