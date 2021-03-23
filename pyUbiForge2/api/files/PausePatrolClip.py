from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PausePatrolClip(SubclassBaseFile):
    ResourceType = 0xB5C32122
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
