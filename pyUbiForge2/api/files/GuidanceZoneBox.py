from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceZone import GuidanceZone as _GuidanceZone


class GuidanceZoneBox(SubclassBaseFile):
    ResourceType = 0x721E514F
    ParentResourceType = _GuidanceZone.ResourceType
    parent: _GuidanceZone

