from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TimedSwitchEvent_LGS(SubclassBaseFile):
    ResourceType = 0x54546F95
    ParentResourceType = _Event.ResourceType
    parent: _Event

