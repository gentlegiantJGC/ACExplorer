from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloorFloat(SubclassBaseFile):
    ResourceType = 0xE0E22F96
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

