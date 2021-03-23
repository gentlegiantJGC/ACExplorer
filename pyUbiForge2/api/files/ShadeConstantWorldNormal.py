from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantWorldNormal(SubclassBaseFile):
    ResourceType = 0x301D571F
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
