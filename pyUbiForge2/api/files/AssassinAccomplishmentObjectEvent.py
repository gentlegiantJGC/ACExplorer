from pyUbiForge2.api.game import SubclassBaseFile
from .AssassinAccomplishmentEvent import AssassinAccomplishmentEvent as _AssassinAccomplishmentEvent


class AssassinAccomplishmentObjectEvent(SubclassBaseFile):
    ResourceType = 0x4AAD1A9C
    ParentResourceType = _AssassinAccomplishmentEvent.ResourceType
    parent: _AssassinAccomplishmentEvent

