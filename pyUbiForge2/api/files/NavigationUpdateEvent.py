from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NavigationUpdateEvent(SubclassBaseFile):
    ResourceType = 0xCABB419D
    ParentResourceType = _Event.ResourceType
    parent: _Event

