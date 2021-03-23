from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FightTutorialClip(SubclassBaseFile):
    ResourceType = 0x44462494
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

