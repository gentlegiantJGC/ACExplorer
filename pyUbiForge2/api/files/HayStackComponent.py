from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class HayStackComponent(SubclassBaseFile):
    ResourceType = 0xCA59EAD5
    ParentResourceType = _Component.ResourceType
    parent: _Component
