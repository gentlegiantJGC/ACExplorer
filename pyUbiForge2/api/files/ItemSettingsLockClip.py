from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ItemSettingsLockClip(SubclassBaseFile):
    ResourceType = 0x2AAF355F
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
