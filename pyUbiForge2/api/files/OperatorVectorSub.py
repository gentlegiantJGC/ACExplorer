from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorSub(SubclassBaseFile):
    ResourceType = 0xC4B80C27
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
