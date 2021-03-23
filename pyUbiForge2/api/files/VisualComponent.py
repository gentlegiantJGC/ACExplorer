from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class VisualComponent(SubclassBaseFile):
    ResourceType = 0x956B3FBC
    ParentResourceType = _Component.ResourceType
    parent: _Component

