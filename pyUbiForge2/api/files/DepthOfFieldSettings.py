from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class DepthOfFieldSettings(SubclassBaseFile):
    ResourceType = 0x6579DF3E
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

