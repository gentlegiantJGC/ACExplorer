from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class GameplayPupetteerClip(SubclassBaseFile):
    ResourceType = 0x5BF55F5F
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

