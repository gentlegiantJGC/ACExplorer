from pyUbiForge2.api.game import SubclassBaseFile
from .TextureBase import TextureBase as _TextureBase


class TextureMapSpec(SubclassBaseFile):
    ResourceType = 0x989DC6B2
    ParentResourceType = _TextureBase.ResourceType
    parent: _TextureBase
