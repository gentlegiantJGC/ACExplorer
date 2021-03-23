from pyUbiForge2.api.game import SubclassBaseFile
from .Zone import Zone as _Zone


class DetectionZone(SubclassBaseFile):
    ResourceType = 0x1663A759
    ParentResourceType = _Zone.ResourceType
    parent: _Zone
