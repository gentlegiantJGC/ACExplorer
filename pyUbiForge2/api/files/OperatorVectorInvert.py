from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class OperatorVectorInvert(SubclassBaseFile):
    ResourceType = 0xC5371D3D
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

