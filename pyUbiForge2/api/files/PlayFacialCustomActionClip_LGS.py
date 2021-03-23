from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PlayFacialCustomActionClip_LGS(SubclassBaseFile):
    ResourceType = 0x637B4989
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
