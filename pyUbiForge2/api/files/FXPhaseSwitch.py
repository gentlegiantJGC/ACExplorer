from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class FXPhaseSwitch(SubclassBaseFile):
    ResourceType = 0xFB2B32FD
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

