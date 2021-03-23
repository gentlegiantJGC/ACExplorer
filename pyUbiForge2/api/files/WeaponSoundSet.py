from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSet import SoundSet as _SoundSet


class WeaponSoundSet(SubclassBaseFile):
    ResourceType = 0x37DF4185
    ParentResourceType = _SoundSet.ResourceType
    parent: _SoundSet

