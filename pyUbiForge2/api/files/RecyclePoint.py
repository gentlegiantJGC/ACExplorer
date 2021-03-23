from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class RecyclePoint(SubclassBaseFile):
    ResourceType = 0xB1CB2060
    ParentResourceType = _Component.ResourceType
    parent: _Component
