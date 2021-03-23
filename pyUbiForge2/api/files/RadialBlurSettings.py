from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class RadialBlurSettings(SubclassBaseFile):
    ResourceType = 0x6FB71F68
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

