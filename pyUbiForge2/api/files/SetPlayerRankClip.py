from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SetPlayerRankClip(SubclassBaseFile):
    ResourceType = 0xB9938679
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

