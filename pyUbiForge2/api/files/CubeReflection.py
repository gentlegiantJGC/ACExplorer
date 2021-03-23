from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class CubeReflection(SubclassBaseFile):
    ResourceType = 0x324ADE83
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
