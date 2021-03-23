from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class CumulativeBuffer(SubclassBaseFile):
    ResourceType = 0xC5CF88C1
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

