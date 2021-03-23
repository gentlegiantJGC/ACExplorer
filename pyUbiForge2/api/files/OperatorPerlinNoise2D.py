from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorPerlinNoise2D(SubclassBaseFile):
    ResourceType = 0x7E87F161
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
