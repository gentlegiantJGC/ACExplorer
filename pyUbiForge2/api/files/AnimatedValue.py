from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class AnimatedValue(SubclassBaseFile):
    ResourceType = 0x92F13269
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
