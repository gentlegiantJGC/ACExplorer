from pyUbiForge2.api.game import SubclassBaseFile
from .MissionIntroActivatorStep import (
    MissionIntroActivatorStep as _MissionIntroActivatorStep,
)


class CrowdMissionAssassinationIntroStep(SubclassBaseFile):
    ResourceType = 0x825607B0
    ParentResourceType = _MissionIntroActivatorStep.ResourceType
    parent: _MissionIntroActivatorStep
