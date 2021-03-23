from pyUbiForge2.api.game import SubclassBaseFile
from .MissionSliceInfo import MissionSliceInfo as _MissionSliceInfo


class MainSliceInfo(SubclassBaseFile):
    ResourceType = 0xE56D0E83
    ParentResourceType = _MissionSliceInfo.ResourceType
    parent: _MissionSliceInfo

