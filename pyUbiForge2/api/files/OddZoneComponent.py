from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class OddZoneComponent(SubclassBaseFile):
    ResourceType = 0x60651D59
    ParentResourceType = _Component.ResourceType
    parent: _Component
