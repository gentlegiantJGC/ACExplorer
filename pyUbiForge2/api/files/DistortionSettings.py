from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class DistortionSettings(SubclassBaseFile):
    ResourceType = 0x7F8BFBCB
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

