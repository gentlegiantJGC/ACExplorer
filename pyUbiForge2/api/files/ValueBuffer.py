from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ValueBuffer(SubclassBaseFile):
    ResourceType = 0xC5F413A4
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

