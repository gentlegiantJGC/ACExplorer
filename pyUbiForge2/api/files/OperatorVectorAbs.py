from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorAbs(SubclassBaseFile):
    ResourceType = 0xB429DF5D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

