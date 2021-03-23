from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class AttackConditionClip(SubclassBaseFile):
    ResourceType = 0x273C2EC8
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

