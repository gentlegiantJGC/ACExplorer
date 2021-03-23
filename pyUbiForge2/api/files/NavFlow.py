from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class NavFlow(SubclassBaseFile):
    ResourceType = 0xEFD4BE98
    ParentResourceType = _Component.ResourceType
    parent: _Component

