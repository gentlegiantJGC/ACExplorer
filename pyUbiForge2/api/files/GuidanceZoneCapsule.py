from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceZone import GuidanceZone as _GuidanceZone


class GuidanceZoneCapsule(SubclassBaseFile):
    ResourceType = 0x962AC98F
    ParentResourceType = _GuidanceZone.ResourceType
    parent: _GuidanceZone

