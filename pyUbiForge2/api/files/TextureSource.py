from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class TextureSource(SubclassBaseFile):
    ResourceType = 0xA9DE3EFA
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

