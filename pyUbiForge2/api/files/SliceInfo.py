from pyUbiForge2.api.game import SubclassBaseFile
from .MemoryInfo import MemoryInfo as _MemoryInfo


class SliceInfo(SubclassBaseFile):
    ResourceType = 0xA1F11163
    ParentResourceType = _MemoryInfo.ResourceType
    parent: _MemoryInfo
