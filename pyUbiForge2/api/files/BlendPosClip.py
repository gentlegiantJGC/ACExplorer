from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class BlendPosClip(SubclassBaseFile):
    ResourceType = 0x42DE7ADE
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
