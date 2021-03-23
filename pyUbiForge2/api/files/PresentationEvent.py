from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PresentationEvent(SubclassBaseFile):
    ResourceType = 0x8F4EC70D
    ParentResourceType = _Event.ResourceType
    parent: _Event

