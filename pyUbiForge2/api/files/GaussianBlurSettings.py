from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class GaussianBlurSettings(SubclassBaseFile):
    ResourceType = 0x6B2C9F07
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
