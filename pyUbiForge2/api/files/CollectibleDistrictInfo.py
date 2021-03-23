from pyUbiForge2.api.game import SubclassBaseFile
from .MemoryInfo import MemoryInfo as _MemoryInfo


class CollectibleDistrictInfo(SubclassBaseFile):
    ResourceType = 0x530E8350
    ParentResourceType = _MemoryInfo.ResourceType
    parent: _MemoryInfo

