from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceObjectOperation import GuidanceObjectOperation as _GuidanceObjectOperation


class GuidanceObjectModified(SubclassBaseFile):
    ResourceType = 0x62A0A6BC
    ParentResourceType = _GuidanceObjectOperation.ResourceType
    parent: _GuidanceObjectOperation

