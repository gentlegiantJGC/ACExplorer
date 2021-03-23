from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ChangeWorldGateClip(SubclassBaseFile):
    ResourceType = 0x5986CB50
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
