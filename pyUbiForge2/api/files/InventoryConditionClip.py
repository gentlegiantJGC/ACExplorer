from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class InventoryConditionClip(SubclassBaseFile):
    ResourceType = 0x63323D98
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
