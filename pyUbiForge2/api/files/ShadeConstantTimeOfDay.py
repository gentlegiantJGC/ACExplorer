from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class ShadeConstantTimeOfDay(SubclassBaseFile):
    ResourceType = 0x7F0B9924
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
