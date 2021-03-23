from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorTruncateVector(SubclassBaseFile):
    ResourceType = 0xEF889D0B
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

