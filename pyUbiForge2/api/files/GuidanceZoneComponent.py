from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GuidanceZoneComponent(SubclassBaseFile):
    ResourceType = 0xA6225373
    ParentResourceType = _Component.ResourceType
    parent: _Component

