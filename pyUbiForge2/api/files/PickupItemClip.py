from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PickupItemClip(SubclassBaseFile):
    ResourceType = 0x881424CF
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

