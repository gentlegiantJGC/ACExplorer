from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class WeaponSelectorClip(SubclassBaseFile):
    ResourceType = 0x8D95D2CE
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

