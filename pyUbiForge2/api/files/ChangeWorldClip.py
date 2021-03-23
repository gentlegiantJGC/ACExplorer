from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ChangeWorldClip(SubclassBaseFile):
    ResourceType = 0xB42B56FD
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
