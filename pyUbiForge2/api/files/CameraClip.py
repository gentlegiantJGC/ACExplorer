from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CameraClip(SubclassBaseFile):
    ResourceType = 0x81910168
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
