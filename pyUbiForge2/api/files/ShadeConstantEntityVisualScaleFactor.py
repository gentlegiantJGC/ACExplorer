from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantEntityVisualScaleFactor(SubclassBaseFile):
    ResourceType = 0xC284C764
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

