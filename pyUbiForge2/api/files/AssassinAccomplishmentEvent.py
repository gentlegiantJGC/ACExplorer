from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentEvent import AccomplishmentEvent as _AccomplishmentEvent


class AssassinAccomplishmentEvent(SubclassBaseFile):
    ResourceType = 0x25AC3F0A
    ParentResourceType = _AccomplishmentEvent.ResourceType
    parent: _AccomplishmentEvent

