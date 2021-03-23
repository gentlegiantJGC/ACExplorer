from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorMin(SubclassBaseFile):
    ResourceType = 0x3DC1932B
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
