from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class PickableComponent(SubclassBaseFile):
    ResourceType = 0xA06E18EE
    ParentResourceType = _Component.ResourceType
    parent: _Component

