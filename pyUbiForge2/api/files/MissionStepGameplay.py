from pyUbiForge2.api.game import SubclassBaseFile
from .MissionStep import MissionStep as _MissionStep


class MissionStepGameplay(SubclassBaseFile):
    ResourceType = 0x32EC84B2
    ParentResourceType = _MissionStep.ResourceType
    parent: _MissionStep
