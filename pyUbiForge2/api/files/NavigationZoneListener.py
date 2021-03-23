from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class NavigationZoneListener(SubclassBaseFile):
    ResourceType = 0x8D9B73E0
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
