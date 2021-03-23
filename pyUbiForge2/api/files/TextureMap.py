from pyUbiForge2.api.game import SubclassBaseFile
from .TextureBase import TextureBase as _TextureBase


class TextureMap(SubclassBaseFile):
    ResourceType = 0xA2B7E917
    ParentResourceType = _TextureBase.ResourceType
    parent: _TextureBase
