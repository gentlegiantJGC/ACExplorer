from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class NothingClip(SubclassBaseFile):
    ResourceType = 0x4A805D2B
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

