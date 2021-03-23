from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SpeechEventClip(SubclassBaseFile):
    ResourceType = 0x3F3D097C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
