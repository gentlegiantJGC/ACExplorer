from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class UnlockShopUpgradeClip(SubclassBaseFile):
    ResourceType = 0x5B9463CA
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

