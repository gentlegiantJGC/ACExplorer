from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepGameplay import MissionStepGameplay as _MissionStepGameplay


class MissionStepCoordinator(SubclassBaseFile):
    ResourceType = 0xE26735FC
    ParentResourceType = _MissionStepGameplay.ResourceType
    parent: _MissionStepGameplay
