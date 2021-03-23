from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class GroupConditionClip(SubclassBaseFile):
    ResourceType = 0x5102704F
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

