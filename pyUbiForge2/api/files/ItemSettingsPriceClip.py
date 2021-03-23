from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ItemSettingsPriceClip(SubclassBaseFile):
    ResourceType = 0xB78B3B62
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

