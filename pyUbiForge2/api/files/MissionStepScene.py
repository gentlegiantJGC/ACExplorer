from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStepGameplay import MissionStepGameplay as _MissionStepGameplay


class MissionStepScene(SubclassBaseFile):
    ResourceType = 0xB8F99093
    ParentResourceType = _MissionStepGameplay.ResourceType
    parent: _MissionStepGameplay

