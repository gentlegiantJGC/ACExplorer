from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantWorldTangent(SubclassBaseFile):
    ResourceType = 0x0E64B843
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

