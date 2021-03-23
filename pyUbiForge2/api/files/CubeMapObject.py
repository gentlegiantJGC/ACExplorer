from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class CubeMapObject(SubclassBaseFile):
    ResourceType = 0x4D9B36E9
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

