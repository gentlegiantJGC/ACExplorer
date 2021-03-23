from pyUbiForge2.api.game import SubclassBaseFile
from .DetectionZone import DetectionZone as _DetectionZone


class DetectionAabb(SubclassBaseFile):
    ResourceType = 0xA9348062
    ParentResourceType = _DetectionZone.ResourceType
    parent: _DetectionZone
