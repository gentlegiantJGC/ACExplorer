from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class VillaContextualAFSClip(SubclassBaseFile):
    ResourceType = 0x31B27B25
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
