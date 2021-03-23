from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoRepositoryEntry import UiInfoRepositoryEntry as _UiInfoRepositoryEntry


class MemoryInfo(SubclassBaseFile):
    ResourceType = 0x50FDC6EA
    ParentResourceType = _UiInfoRepositoryEntry.ResourceType
    parent: _UiInfoRepositoryEntry

