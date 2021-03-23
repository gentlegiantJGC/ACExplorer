from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CinematicCameraClip(SubclassBaseFile):
    ResourceType = 0x913E0C46
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

