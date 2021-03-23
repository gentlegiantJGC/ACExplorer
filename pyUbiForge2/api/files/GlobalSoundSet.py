from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSet import SoundSet as _SoundSet


class GlobalSoundSet(SubclassBaseFile):
    ResourceType = 0xF96CC120
    ParentResourceType = _SoundSet.ResourceType
    parent: _SoundSet
