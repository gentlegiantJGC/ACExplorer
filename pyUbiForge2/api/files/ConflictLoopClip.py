from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ConflictLoopClip(SubclassBaseFile):
    ResourceType = 0xAA5F263C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
