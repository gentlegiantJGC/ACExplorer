from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class MoneyClip(SubclassBaseFile):
    ResourceType = 0x9B3B0D43
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
