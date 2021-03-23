from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ConstantValue(SubclassBaseFile):
    ResourceType = 0xAA890185
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
