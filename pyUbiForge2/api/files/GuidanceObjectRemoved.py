from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceObjectOperation import GuidanceObjectOperation as _GuidanceObjectOperation


class GuidanceObjectRemoved(SubclassBaseFile):
    ResourceType = 0xAD333D18
    ParentResourceType = _GuidanceObjectOperation.ResourceType
    parent: _GuidanceObjectOperation

