from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class TextureOverlaySettings(SubclassBaseFile):
    ResourceType = 0x720F4B4E
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
