from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PauseFightClip(SubclassBaseFile):
    ResourceType = 0x21ACA0A8
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
