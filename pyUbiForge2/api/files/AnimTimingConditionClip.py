from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class AnimTimingConditionClip(SubclassBaseFile):
    ResourceType = 0xFBD5AD7F
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
