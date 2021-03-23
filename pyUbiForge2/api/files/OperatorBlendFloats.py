from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorBlendFloats(SubclassBaseFile):
    ResourceType = 0xEFD14B23
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

