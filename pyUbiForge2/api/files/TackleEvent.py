from pyUbiForge2.api.game import SubclassBaseFile
from .PresentationEvent import PresentationEvent as _PresentationEvent


class TackleEvent(SubclassBaseFile):
    ResourceType = 0x5DC81B4E
    ParentResourceType = _PresentationEvent.ResourceType
    parent: _PresentationEvent
