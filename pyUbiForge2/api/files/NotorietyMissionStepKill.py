from pyUbiForge2.api.game import SubclassBaseFile
from .NotorietyMissionStep import NotorietyMissionStep as _NotorietyMissionStep


class NotorietyMissionStepKill(SubclassBaseFile):
    ResourceType = 0x939007D0
    ParentResourceType = _NotorietyMissionStep.ResourceType
    parent: _NotorietyMissionStep
