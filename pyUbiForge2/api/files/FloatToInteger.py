from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FloatToInteger(SubclassBaseFile):
    ResourceType = 0xE61CD6C2
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

