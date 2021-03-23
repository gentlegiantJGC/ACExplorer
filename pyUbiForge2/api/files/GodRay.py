from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GodRay(SubclassBaseFile):
    ResourceType = 0x36BE721F
    ParentResourceType = _Component.ResourceType
    parent: _Component
