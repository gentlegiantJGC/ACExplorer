from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BuildingUpgradedEvent(SubclassBaseFile):
    ResourceType = 0x8BBD2BE2
    ParentResourceType = _Event.ResourceType
    parent: _Event
