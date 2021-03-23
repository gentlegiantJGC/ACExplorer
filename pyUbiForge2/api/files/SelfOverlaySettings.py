from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class SelfOverlaySettings(SubclassBaseFile):
    ResourceType = 0xBE81DF9F
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
