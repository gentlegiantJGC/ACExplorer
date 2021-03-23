from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantEntityToCameraDistance(SubclassBaseFile):
    ResourceType = 0xD6004EC3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
