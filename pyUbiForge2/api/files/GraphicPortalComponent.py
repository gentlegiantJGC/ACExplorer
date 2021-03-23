from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GraphicPortalComponent(SubclassBaseFile):
    ResourceType = 0xD5E907BD
    ParentResourceType = _Component.ResourceType
    parent: _Component
