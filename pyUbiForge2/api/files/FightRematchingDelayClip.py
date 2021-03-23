from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FightRematchingDelayClip(SubclassBaseFile):
    ResourceType = 0x76D5186A
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

