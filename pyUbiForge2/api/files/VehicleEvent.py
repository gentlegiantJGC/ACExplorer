from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VehicleEvent(SubclassBaseFile):
    ResourceType = 0xCDE6BD1C
    ParentResourceType = _Event.ResourceType
    parent: _Event
