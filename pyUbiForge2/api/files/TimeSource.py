from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class TimeSource(SubclassBaseFile):
    ResourceType = 0xD8317475
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
