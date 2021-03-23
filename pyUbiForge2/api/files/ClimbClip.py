from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ClimbClip(SubclassBaseFile):
    ResourceType = 0xE3B2CB42
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

