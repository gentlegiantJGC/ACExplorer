from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class PlayerRespawnEventConditionClip(SubclassBaseFile):
    ResourceType = 0x10E3C5D2
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
