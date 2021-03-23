from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class NavigationZone(SubclassBaseFile):
    ResourceType = 0xD8388CF0
    ParentResourceType = _Component.ResourceType
    parent: _Component

