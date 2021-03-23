from pyUbiForge2.api.game import SubclassBaseFile
from .SoundSet import SoundSet as _SoundSet


class ProjectileSoundSet(SubclassBaseFile):
    ResourceType = 0xF57C4D33
    ParentResourceType = _SoundSet.ResourceType
    parent: _SoundSet

