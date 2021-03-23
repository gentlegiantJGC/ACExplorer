from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantLODBlendFactor(SubclassBaseFile):
    ResourceType = 0x2A8456D3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

