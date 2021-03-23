from pyUbiForge2.api.game import SubclassBaseFile
from .PresentationEvent import PresentationEvent as _PresentationEvent


class FallEvent(SubclassBaseFile):
    ResourceType = 0x58ADF508
    ParentResourceType = _PresentationEvent.ResourceType
    parent: _PresentationEvent

