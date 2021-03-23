from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GraphicAntiPortalComponent(SubclassBaseFile):
    ResourceType = 0xC4F2A686
    ParentResourceType = _Component.ResourceType
    parent: _Component
