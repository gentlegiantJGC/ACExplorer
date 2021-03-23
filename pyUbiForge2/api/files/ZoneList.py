from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class ZoneList(SubclassBaseFile):
    ResourceType = 0x7AA81246
    ParentResourceType = _Component.ResourceType
    parent: _Component
