from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoRepositoryEntry import UiInfoRepositoryEntry as _UiInfoRepositoryEntry


class UIInventoryInfo(SubclassBaseFile):
    ResourceType = 0x6692B46F
    ParentResourceType = _UiInfoRepositoryEntry.ResourceType
    parent: _UiInfoRepositoryEntry

