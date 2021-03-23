from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSet import SoundSet as _SoundSet


class HumanSoundSet(SubclassBaseFile):
    ResourceType = 0x2B315BEA
    ParentResourceType = _SoundSet.ResourceType
    parent: _SoundSet

