from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentEvent import AccomplishmentEvent as _AccomplishmentEvent


class AccomplishmentMissionEvent(SubclassBaseFile):
    ResourceType = 0xB59BE2B6
    ParentResourceType = _AccomplishmentEvent.ResourceType
    parent: _AccomplishmentEvent

