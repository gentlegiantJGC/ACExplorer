from pyUbiForge2.api.game import SubclassBaseFile
from .PresentationEvent import PresentationEvent as _PresentationEvent


class BlendEvent(SubclassBaseFile):
    ResourceType = 0x2F38CBCE
    ParentResourceType = _PresentationEvent.ResourceType
    parent: _PresentationEvent

