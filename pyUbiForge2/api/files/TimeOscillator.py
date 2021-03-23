from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class TimeOscillator(SubclassBaseFile):
    ResourceType = 0xB829D5C7
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
