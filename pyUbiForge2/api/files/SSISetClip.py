from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SSISetClip(SubclassBaseFile):
    ResourceType = 0xA6A4BEC1
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
