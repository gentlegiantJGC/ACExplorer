from pyUbiForge2.api.game import SubclassBaseFile
from .MissionIntroActivatorStep import (
    MissionIntroActivatorStep as _MissionIntroActivatorStep,
)


class NotorietyMissionStepPosters(SubclassBaseFile):
    ResourceType = 0x93028F01
    ParentResourceType = _MissionIntroActivatorStep.ResourceType
    parent: _MissionIntroActivatorStep
