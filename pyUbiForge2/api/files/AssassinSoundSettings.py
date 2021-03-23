from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSettings import SoundSettings as _SoundSettings


class AssassinSoundSettings(SubclassBaseFile):
    ResourceType = 0xFD9CF1E7
    ParentResourceType = _SoundSettings.ResourceType
    parent: _SoundSettings

