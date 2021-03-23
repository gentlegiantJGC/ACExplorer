from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepCoordinator import MissionStepCoordinator as _MissionStepCoordinator


class MissionStepWhiteRoomActivator(SubclassBaseFile):
    ResourceType = 0x1124EF02
    ParentResourceType = _MissionStepCoordinator.ResourceType
    parent: _MissionStepCoordinator
