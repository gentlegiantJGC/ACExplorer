from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class DynamicActionBlockPusher(SubclassBaseFile):
    ResourceType = 0x1C6A7627
    ParentResourceType = _Component.ResourceType
    parent: _Component

