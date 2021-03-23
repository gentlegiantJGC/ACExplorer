from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class EdgeBloomSettings(SubclassBaseFile):
    ResourceType = 0x9B42511B
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

