from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorCeilFloat(SubclassBaseFile):
    ResourceType = 0xE206C788
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
