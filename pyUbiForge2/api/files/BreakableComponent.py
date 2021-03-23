from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class BreakableComponent(SubclassBaseFile):
    ResourceType = 0x44F8FD99
    ParentResourceType = _Component.ResourceType
    parent: _Component

