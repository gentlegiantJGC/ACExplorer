from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class DropItemClip(SubclassBaseFile):
    ResourceType = 0x05895954
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
