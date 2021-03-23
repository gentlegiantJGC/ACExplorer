from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorReciprocalFloat(SubclassBaseFile):
    ResourceType = 0xF777C0E3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
