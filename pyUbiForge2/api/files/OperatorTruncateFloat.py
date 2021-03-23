from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorTruncateFloat(SubclassBaseFile):
    ResourceType = 0xFBC55F83
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

