from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStep import MissionStep as _MissionStep


class MissionIntroActivatorStep(SubclassBaseFile):
    ResourceType = 0x10856DE1
    ParentResourceType = _MissionStep.ResourceType
    parent: _MissionStep

