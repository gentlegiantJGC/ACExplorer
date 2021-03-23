from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ResetBehaviorClip(SubclassBaseFile):
    ResourceType = 0x27CAB3D3
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

