from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceZone import GuidanceZone as _GuidanceZone


class GuidanceZoneSphere(SubclassBaseFile):
    ResourceType = 0xC9C64371
    ParentResourceType = _GuidanceZone.ResourceType
    parent: _GuidanceZone

