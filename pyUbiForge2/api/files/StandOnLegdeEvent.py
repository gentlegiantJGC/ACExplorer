from pyUbiForge2.api.game import SubclassBaseFile
from .PresentationEvent import PresentationEvent as _PresentationEvent


class StandOnLegdeEvent(SubclassBaseFile):
    ResourceType = 0xBA78663D
    ParentResourceType = _PresentationEvent.ResourceType
    parent: _PresentationEvent
