from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class GlowEffectSettings(SubclassBaseFile):
    ResourceType = 0x93DDEAC0
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
