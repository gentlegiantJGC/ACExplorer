from pyUbiForge2.api.game import SubclassBaseFile
from .TextureBase import TextureBase as _TextureBase


class TextureSelector(SubclassBaseFile):
    ResourceType = 0x7D08460D
    ParentResourceType = _TextureBase.ResourceType
    parent: _TextureBase
