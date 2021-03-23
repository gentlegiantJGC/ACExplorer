from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FXElementOperator(SubclassBaseFile):
    ResourceType = 0x7AB22DED
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

