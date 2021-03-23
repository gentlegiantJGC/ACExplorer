from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class LinkedValue(SubclassBaseFile):
    ResourceType = 0xD3785D86
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
