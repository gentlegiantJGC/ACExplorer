from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class EventListenerComponent(SubclassBaseFile):
    ResourceType = 0x2AA179AB
    ParentResourceType = _Component.ResourceType
    parent: _Component

