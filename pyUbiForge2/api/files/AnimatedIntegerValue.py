from pyUbiForge2.api.game import SubclassBaseFile
from .AnimatedValue import AnimatedValue as _AnimatedValue


class AnimatedIntegerValue(SubclassBaseFile):
    ResourceType = 0x1AF56DD2
    ParentResourceType = _AnimatedValue.ResourceType
    parent: _AnimatedValue
