from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DLCAlternateIconCoordinatorEvent(SubclassBaseFile):
    ResourceType = 0xC0E1DEC8
    ParentResourceType = _Event.ResourceType
    parent: _Event

