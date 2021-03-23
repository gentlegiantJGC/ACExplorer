from pyUbiForge2.api.game import SubclassBaseFile
from .DetectionComponent import DetectionComponent as _DetectionComponent


class TargettingComponent(SubclassBaseFile):
    ResourceType = 0x40D05488
    ParentResourceType = _DetectionComponent.ResourceType
    parent: _DetectionComponent

