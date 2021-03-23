from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class DeathConditionClip(SubclassBaseFile):
    ResourceType = 0x40D54702
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

