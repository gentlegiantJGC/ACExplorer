from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class GlitcherSettings(SubclassBaseFile):
    ResourceType = 0x45603FBE
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

