from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class DetectionComponent(SubclassBaseFile):
    ResourceType = 0x35955C41
    ParentResourceType = _Component.ResourceType
    parent: _Component
