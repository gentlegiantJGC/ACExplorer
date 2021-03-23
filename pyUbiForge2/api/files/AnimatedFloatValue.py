from pyUbiForge2.api.game import SubclassBaseFile
from .AnimatedValue import AnimatedValue as _AnimatedValue


class AnimatedFloatValue(SubclassBaseFile):
    ResourceType = 0xE6B2ABE6
    ParentResourceType = _AnimatedValue.ResourceType
    parent: _AnimatedValue
