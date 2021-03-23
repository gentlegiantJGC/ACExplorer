from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class FadeEffectSettings(SubclassBaseFile):
    ResourceType = 0xD80EFA50
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
