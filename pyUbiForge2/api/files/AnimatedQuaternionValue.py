from pyUbiForge2.api.game import SubclassBaseFile
from .AnimatedValue import AnimatedValue as _AnimatedValue


class AnimatedQuaternionValue(SubclassBaseFile):
    ResourceType = 0x41922A2D
    ParentResourceType = _AnimatedValue.ResourceType
    parent: _AnimatedValue

