from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepScheduler import MissionStepScheduler as _MissionStepScheduler


class MissionStepConcurrentScheduler(SubclassBaseFile):
    ResourceType = 0x299F8BE6
    ParentResourceType = _MissionStepScheduler.ResourceType
    parent: _MissionStepScheduler
