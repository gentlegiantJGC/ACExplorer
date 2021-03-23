from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FightDesiredPositionClip(SubclassBaseFile):
    ResourceType = 0x82B953AB
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

