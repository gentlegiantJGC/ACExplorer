from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class LGSSolvedClip(SubclassBaseFile):
    ResourceType = 0x4C3C8372
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
