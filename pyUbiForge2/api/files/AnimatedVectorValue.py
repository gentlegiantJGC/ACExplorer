from pyUbiForge2.api.game import SubclassBaseFile
from .AnimatedValue import AnimatedValue as _AnimatedValue


class AnimatedVectorValue(SubclassBaseFile):
    ResourceType = 0x67631517
    ParentResourceType = _AnimatedValue.ResourceType
    parent: _AnimatedValue
