from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSet import SoundSet as _SoundSet


class KioskSoundSet(SubclassBaseFile):
    ResourceType = 0xAE493A02
    ParentResourceType = _SoundSet.ResourceType
    parent: _SoundSet
