from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class AIComponent(SubclassBaseFile):
    ResourceType = 0x33E86CF3
    ParentResourceType = _Component.ResourceType
    parent: _Component
