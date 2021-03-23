from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class UIClip(SubclassBaseFile):
    ResourceType = 0x9434669A
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
