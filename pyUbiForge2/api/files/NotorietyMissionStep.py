from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStep import MissionStep as _MissionStep


class NotorietyMissionStep(SubclassBaseFile):
    ResourceType = 0x03A532E4
    ParentResourceType = _MissionStep.ResourceType
    parent: _MissionStep
