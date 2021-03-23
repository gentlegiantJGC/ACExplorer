from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorFloatClamp(SubclassBaseFile):
    ResourceType = 0x0F229EB9
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

