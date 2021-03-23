from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceZone import GuidanceZone as _GuidanceZone


class GuidanceZonePlane(SubclassBaseFile):
    ResourceType = 0xF7907244
    ParentResourceType = _GuidanceZone.ResourceType
    parent: _GuidanceZone

