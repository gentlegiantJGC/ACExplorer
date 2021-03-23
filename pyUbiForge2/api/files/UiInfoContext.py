from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoRepositoryEntry import UiInfoRepositoryEntry as _UiInfoRepositoryEntry


class UiInfoContext(SubclassBaseFile):
    ResourceType = 0x5A3FAE75
    ParentResourceType = _UiInfoRepositoryEntry.ResourceType
    parent: _UiInfoRepositoryEntry

