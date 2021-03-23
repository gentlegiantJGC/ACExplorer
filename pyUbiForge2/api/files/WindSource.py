from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class WindSource(SubclassBaseFile):
    ResourceType = 0x1BFEC321
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
