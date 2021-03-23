from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VillaAfterSaveGameLoadedEvent(SubclassBaseFile):
    ResourceType = 0x5202C27D
    ParentResourceType = _Event.ResourceType
    parent: _Event

