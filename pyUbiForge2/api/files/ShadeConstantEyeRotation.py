from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantEyeRotation(SubclassBaseFile):
    ResourceType = 0xFEE8C0BF
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

