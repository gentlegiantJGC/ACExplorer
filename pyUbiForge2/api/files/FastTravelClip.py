from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FastTravelClip(SubclassBaseFile):
    ResourceType = 0x73745C9B
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
