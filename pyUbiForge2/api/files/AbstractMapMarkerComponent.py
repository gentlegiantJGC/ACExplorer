from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class AbstractMapMarkerComponent(SubclassBaseFile):
    ResourceType = 0xFECB0A9F
    ParentResourceType = _Component.ResourceType
    parent: _Component

