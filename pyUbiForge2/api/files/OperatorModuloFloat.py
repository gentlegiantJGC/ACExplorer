from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorModuloFloat(SubclassBaseFile):
    ResourceType = 0x8873E1B7
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

