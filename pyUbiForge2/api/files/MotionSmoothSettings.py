from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class MotionSmoothSettings(SubclassBaseFile):
    ResourceType = 0x864DC837
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
