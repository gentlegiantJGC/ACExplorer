from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class AnimusDatabaseGlyphConditionClip(SubclassBaseFile):
    ResourceType = 0xB3A6BA93
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

