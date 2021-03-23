from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SoftBodyComponent(SubclassBaseFile):
    ResourceType = 0xB48EBA69
    ParentResourceType = _Component.ResourceType
    parent: _Component

