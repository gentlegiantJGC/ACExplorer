from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NavigationSpeedAndDirEvent(SubclassBaseFile):
    ResourceType = 0x2F9C0949
    ParentResourceType = _Event.ResourceType
    parent: _Event
