from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceObjectOperation import GuidanceObjectOperation as _GuidanceObjectOperation


class GuidanceObjectAdded(SubclassBaseFile):
    ResourceType = 0x97916D86
    ParentResourceType = _GuidanceObjectOperation.ResourceType
    parent: _GuidanceObjectOperation

