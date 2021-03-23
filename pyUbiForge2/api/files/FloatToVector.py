from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FloatToVector(SubclassBaseFile):
    ResourceType = 0x6E909BEA
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
