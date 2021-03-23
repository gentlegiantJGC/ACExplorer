from pyUbiForge2.api.game import SubclassBaseFile
from .DetectionZone import DetectionZone as _DetectionZone


class DetectionShape(SubclassBaseFile):
    ResourceType = 0x51550B4C
    ParentResourceType = _DetectionZone.ResourceType
    parent: _DetectionZone

