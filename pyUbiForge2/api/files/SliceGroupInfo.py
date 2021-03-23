from pyUbiForge2.api.game import SubclassBaseFile
from .MemoryInfo import MemoryInfo as _MemoryInfo


class SliceGroupInfo(SubclassBaseFile):
    ResourceType = 0x94216457
    ParentResourceType = _MemoryInfo.ResourceType
    parent: _MemoryInfo

