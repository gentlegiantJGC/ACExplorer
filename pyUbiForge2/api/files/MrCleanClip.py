from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class MrCleanClip(SubclassBaseFile):
    ResourceType = 0xF4CE2843
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
