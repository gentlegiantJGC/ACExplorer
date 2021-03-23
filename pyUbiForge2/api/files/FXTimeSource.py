from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FXTimeSource(SubclassBaseFile):
    ResourceType = 0x5D4DF41D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

