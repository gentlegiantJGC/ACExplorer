from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class FocusConditionClip(SubclassBaseFile):
    ResourceType = 0x60FC0AD2
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

