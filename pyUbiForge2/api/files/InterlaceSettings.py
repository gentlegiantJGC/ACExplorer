from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class InterlaceSettings(SubclassBaseFile):
    ResourceType = 0x5B1DF2EF
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

