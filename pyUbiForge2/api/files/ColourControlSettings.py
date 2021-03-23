from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class ColourControlSettings(SubclassBaseFile):
    ResourceType = 0x583F4578
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect
