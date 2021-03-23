from pyUbiForge2.api.game import SubclassBaseFile
from .SliceInfo import SliceInfo as _SliceInfo


class MissionSliceInfo(SubclassBaseFile):
    ResourceType = 0x90F22EC7
    ParentResourceType = _SliceInfo.ResourceType
    parent: _SliceInfo
