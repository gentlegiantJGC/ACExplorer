from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class HideClip(SubclassBaseFile):
    ResourceType = 0x6F95DE33
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
