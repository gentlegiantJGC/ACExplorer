from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FightUpBeatClip(SubclassBaseFile):
    ResourceType = 0xF078ED3E
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
