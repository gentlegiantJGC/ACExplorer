from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GraphicSectorComponent(SubclassBaseFile):
    ResourceType = 0x1423525D
    ParentResourceType = _Component.ResourceType
    parent: _Component

