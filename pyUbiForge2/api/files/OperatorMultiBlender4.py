from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorMultiBlender4(SubclassBaseFile):
    ResourceType = 0xC1BF052D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

