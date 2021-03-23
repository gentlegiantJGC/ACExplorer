from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class VectorsToQuaternion(SubclassBaseFile):
    ResourceType = 0x3060F4B3
    ParentResourceType = _Operator.ResourceType
    parent: _Operator
