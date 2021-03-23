from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ContactEvent(SubclassBaseFile):
    ResourceType = 0x97840CBF
    ParentResourceType = _Event.ResourceType
    parent: _Event

