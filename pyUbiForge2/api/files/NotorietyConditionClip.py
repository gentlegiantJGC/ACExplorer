from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class NotorietyConditionClip(SubclassBaseFile):
    ResourceType = 0xCF169C1D
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

