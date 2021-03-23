from pyUbiForge2.api.game import SubclassBaseFile
from .ReferencingEvent import ReferencingEvent as _ReferencingEvent


class ReferencingConstraintEvent(SubclassBaseFile):
    ResourceType = 0xA045E114
    ParentResourceType = _ReferencingEvent.ResourceType
    parent: _ReferencingEvent

