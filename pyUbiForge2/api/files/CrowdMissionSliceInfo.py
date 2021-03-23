from pyUbiForge2.api.game import SubclassBaseFile
from .AdditionalSliceInfo import AdditionalSliceInfo as _AdditionalSliceInfo


class CrowdMissionSliceInfo(SubclassBaseFile):
    ResourceType = 0xB706A0A0
    ParentResourceType = _AdditionalSliceInfo.ResourceType
    parent: _AdditionalSliceInfo
