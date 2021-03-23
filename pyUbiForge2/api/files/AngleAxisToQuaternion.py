from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class AngleAxisToQuaternion(SubclassBaseFile):
    ResourceType = 0x3610E0C0
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

