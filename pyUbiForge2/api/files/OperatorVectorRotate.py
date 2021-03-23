from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorRotate(SubclassBaseFile):
    ResourceType = 0x00AC21F6
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
