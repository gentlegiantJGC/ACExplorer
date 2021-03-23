from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class EulerToQuaternion(SubclassBaseFile):
    ResourceType = 0x0B4B88D4
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
