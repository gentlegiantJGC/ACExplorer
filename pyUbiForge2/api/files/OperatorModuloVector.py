from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorModuloVector(SubclassBaseFile):
    ResourceType = 0xCE4FDF00
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
