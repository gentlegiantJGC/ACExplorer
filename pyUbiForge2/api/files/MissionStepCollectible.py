from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStep import MissionStep as _MissionStep


class MissionStepCollectible(SubclassBaseFile):
    ResourceType = 0xEA86ACF8
    ParentResourceType = _MissionStep.ResourceType
    parent: _MissionStep

