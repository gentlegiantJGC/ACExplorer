from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TimeOfDayChangedEvent(SubclassBaseFile):
    ResourceType = 0x5210E608
    ParentResourceType = _Event.ResourceType
    parent: _Event