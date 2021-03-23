from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorMultiBlender(SubclassBaseFile):
    ResourceType = 0xD172F62C
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

