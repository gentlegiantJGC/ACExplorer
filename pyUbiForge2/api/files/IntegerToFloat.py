from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class IntegerToFloat(SubclassBaseFile):
    ResourceType = 0xE74A9CC1
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
