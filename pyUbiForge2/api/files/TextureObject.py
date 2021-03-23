from pyUbiForge2.api.game import SubclassBaseFile
from .Operator import Operator as _Operator


class TextureObject(SubclassBaseFile):
    ResourceType = 0x5EF9EA65
    ParentResourceType = _Operator.ResourceType
    parent: _Operator

