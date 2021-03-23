from pyUbiForge2.api.game import SubclassBaseFile
from .TimedClip import TimedClip as _TimedClip


class SoundClip(SubclassBaseFile):
    ResourceType = 0x6857FF64
    ParentResourceType = _TimedClip.ResourceType
    parent: _TimedClip
