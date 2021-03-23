from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorPerlinNoise3D(SubclassBaseFile):
    ResourceType = 0x679CC020
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

