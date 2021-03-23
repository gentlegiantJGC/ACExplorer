from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class DecipherCodexClip(SubclassBaseFile):
    ResourceType = 0xBE0401C8
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
