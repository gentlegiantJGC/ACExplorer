from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SpaceReferenceOverrideClip(SubclassBaseFile):
    ResourceType = 0xF7489A2C
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

