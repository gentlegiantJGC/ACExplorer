from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class WagonHealthConditionClip(SubclassBaseFile):
    ResourceType = 0xC2CB463F
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

