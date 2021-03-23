from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStep import MissionStep as _MissionStep


class MissionStepLanguage(SubclassBaseFile):
    ResourceType = 0xEE8F2182
    ParentResourceType = _MissionStep.ResourceType
    parent: _MissionStep
