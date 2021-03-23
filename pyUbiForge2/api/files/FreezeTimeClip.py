from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FreezeTimeClip(SubclassBaseFile):
    ResourceType = 0xD2298861
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
