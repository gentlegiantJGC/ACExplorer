from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class DesaturateSettings(SubclassBaseFile):
    ResourceType = 0xC16A13E0
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

