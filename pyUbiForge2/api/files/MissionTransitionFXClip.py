from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class MissionTransitionFXClip(SubclassBaseFile):
    ResourceType = 0xAA68DE1E
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
