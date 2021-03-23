from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorMax(SubclassBaseFile):
    ResourceType = 0x01CCAC72
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

