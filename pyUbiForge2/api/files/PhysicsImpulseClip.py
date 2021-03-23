from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PhysicsImpulseClip(SubclassBaseFile):
    ResourceType = 0x90B15247
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

