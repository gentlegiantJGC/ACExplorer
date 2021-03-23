from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class QuaternionToEuler(SubclassBaseFile):
    ResourceType = 0x1EA75879
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
