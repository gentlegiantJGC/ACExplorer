from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class GodRaySettings(SubclassBaseFile):
    ResourceType = 0xCCFE1F35
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

