from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FXContactSource(SubclassBaseFile):
    ResourceType = 0x68BEF262
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

