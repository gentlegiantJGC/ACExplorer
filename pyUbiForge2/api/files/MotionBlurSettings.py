from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class MotionBlurSettings(SubclassBaseFile):
    ResourceType = 0xBBAFC1DB
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

