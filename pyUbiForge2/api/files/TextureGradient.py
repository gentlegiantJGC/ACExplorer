from pyUbiForge2.api.game import SubclassBaseFile
from .TextureMap import TextureMap as _TextureMap


class TextureGradient(SubclassBaseFile):
    ResourceType = 0x245F5CA5
    ParentResourceType = _TextureMap.ResourceType
    parent: _TextureMap
