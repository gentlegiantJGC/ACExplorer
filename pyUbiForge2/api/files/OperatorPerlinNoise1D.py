from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorPerlinNoise1D(SubclassBaseFile):
    ResourceType = 0x55AAA2A2
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
