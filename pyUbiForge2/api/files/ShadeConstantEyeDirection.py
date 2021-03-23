from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantEyeDirection(SubclassBaseFile):
    ResourceType = 0xAFF9297C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

