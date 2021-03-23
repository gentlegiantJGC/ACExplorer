from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AccomplishmentEvent(SubclassBaseFile):
    ResourceType = 0x4836F507
    ParentResourceType = _Event.ResourceType
    parent: _Event
