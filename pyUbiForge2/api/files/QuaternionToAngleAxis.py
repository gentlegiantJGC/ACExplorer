from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class QuaternionToAngleAxis(SubclassBaseFile):
    ResourceType = 0xC1199C46
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
