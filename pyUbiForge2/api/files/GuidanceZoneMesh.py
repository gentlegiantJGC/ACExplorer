from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceZone import GuidanceZone as _GuidanceZone


class GuidanceZoneMesh(SubclassBaseFile):
    ResourceType = 0xC17A08FC
    ParentResourceType = _GuidanceZone.ResourceType
    parent: _GuidanceZone
