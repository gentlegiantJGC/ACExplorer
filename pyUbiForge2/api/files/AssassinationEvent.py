from pyUbiForge2.api.game import SubclassBaseFile
from .PresentationEvent import PresentationEvent as _PresentationEvent


class AssassinationEvent(SubclassBaseFile):
    ResourceType = 0x016BAE37
    ParentResourceType = _PresentationEvent.ResourceType
    parent: _PresentationEvent
