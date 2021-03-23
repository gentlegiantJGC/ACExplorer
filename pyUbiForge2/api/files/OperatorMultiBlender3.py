from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorMultiBlender3(SubclassBaseFile):
    ResourceType = 0x5FDB908E
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
