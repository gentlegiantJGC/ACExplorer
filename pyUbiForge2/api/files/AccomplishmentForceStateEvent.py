from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AccomplishmentForceStateEvent(SubclassBaseFile):
    ResourceType = 0x973530D4
    ParentResourceType = _Event.ResourceType
    parent: _Event
