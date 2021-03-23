from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class RollOffComponent(SubclassBaseFile):
    ResourceType = 0x8CFC6A1A
    ParentResourceType = _Component.ResourceType
    parent: _Component
