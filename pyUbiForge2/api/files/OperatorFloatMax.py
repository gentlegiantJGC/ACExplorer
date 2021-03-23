from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatMax(SubclassBaseFile):
    ResourceType = 0xDB231933
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

