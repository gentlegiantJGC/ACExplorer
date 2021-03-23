from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VanishingSourceEvent(SubclassBaseFile):
    ResourceType = 0xB4855D0A
    ParentResourceType = _Event.ResourceType
    parent: _Event

