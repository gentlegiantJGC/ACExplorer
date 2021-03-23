from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class TimeOfDayClip(SubclassBaseFile):
    ResourceType = 0x63E55773
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

