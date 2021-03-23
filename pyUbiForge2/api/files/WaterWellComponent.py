from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class WaterWellComponent(SubclassBaseFile):
    ResourceType = 0xEFACFB68
    ParentResourceType = _Component.ResourceType
    parent: _Component

