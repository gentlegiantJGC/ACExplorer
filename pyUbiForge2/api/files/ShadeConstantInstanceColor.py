from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantInstanceColor(SubclassBaseFile):
    ResourceType = 0xF1EDEE92
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

