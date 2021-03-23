from pyUbiForge2.api.game import SubclassBaseFile
from .PostEffect import PostEffect as _PostEffect


class ColorBalanceSettings(SubclassBaseFile):
    ResourceType = 0xA8820575
    ParentResourceType = _PostEffect.ResourceType
    parent: _PostEffect

