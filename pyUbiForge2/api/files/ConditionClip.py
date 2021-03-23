from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ConditionClip(SubclassBaseFile):
    ResourceType = 0xBA59E0EF
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

