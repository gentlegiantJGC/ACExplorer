from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStep import MissionStep as _MissionStep


class MissionStepGroup(SubclassBaseFile):
    ResourceType = 0x0C403B8C
    ParentResourceType = _MissionStep.ResourceType
    parent: _MissionStep
