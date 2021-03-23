from pyUbiForge2.api.game import SubclassBaseFile
from .SoundClip import SoundClip as _SoundClip


class ScriptedSoundClip(SubclassBaseFile):
    ResourceType = 0xA6D3C724
    ParentResourceType = _SoundClip.ResourceType
    parent: _SoundClip
