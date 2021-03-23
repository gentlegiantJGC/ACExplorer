from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepGroup import MissionStepGroup as _MissionStepGroup


class MissionStepCountedGroup(SubclassBaseFile):
    ResourceType = 0x72BD8C71
    ParentResourceType = _MissionStepGroup.ResourceType
    parent: _MissionStepGroup
