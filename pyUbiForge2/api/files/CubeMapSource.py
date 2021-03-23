from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class CubeMapSource(SubclassBaseFile):
    ResourceType = 0xBABCE276
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

