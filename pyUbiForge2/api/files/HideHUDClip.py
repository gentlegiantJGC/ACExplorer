from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class HideHUDClip(SubclassBaseFile):
    ResourceType = 0x19F8201D
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
