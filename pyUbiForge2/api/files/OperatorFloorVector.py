from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloorVector(SubclassBaseFile):
    ResourceType = 0x824E5E90
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

