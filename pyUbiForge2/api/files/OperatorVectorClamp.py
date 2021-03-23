from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorClamp(SubclassBaseFile):
    ResourceType = 0x5D4B7D11
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

