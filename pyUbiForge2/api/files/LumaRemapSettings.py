from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class LumaRemapSettings(SubclassBaseFile):
    ResourceType = 0xFE9C38DB
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
