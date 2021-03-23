from pyUbiForge2.api.game import SubclassBaseFile
from .SoundClip import SoundClip as _SoundClip


class SoundPlayClip(SubclassBaseFile):
    ResourceType = 0xA22A1BCD
    ParentResourceType = _SoundClip.ResourceType
    parent: _SoundClip
