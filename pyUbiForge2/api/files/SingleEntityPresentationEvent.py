from pyUbiForge2.api.game import SubclassBaseFile
from .PresentationEvent import PresentationEvent as _PresentationEvent


class SingleEntityPresentationEvent(SubclassBaseFile):
    ResourceType = 0x0A582FB0
    ParentResourceType = _PresentationEvent.ResourceType
    parent: _PresentationEvent

