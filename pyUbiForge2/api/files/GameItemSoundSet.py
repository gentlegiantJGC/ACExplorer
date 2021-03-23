from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSet import SoundSet as _SoundSet


class GameItemSoundSet(SubclassBaseFile):
    ResourceType = 0xDB370F34
    ParentResourceType = _SoundSet.ResourceType
    parent: _SoundSet

