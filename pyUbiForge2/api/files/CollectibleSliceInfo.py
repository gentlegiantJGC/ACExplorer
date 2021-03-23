from pyUbiForge2.api.game import SubclassBaseFile
from .AdditionalSliceInfo import AdditionalSliceInfo as _AdditionalSliceInfo


class CollectibleSliceInfo(SubclassBaseFile):
    ResourceType = 0x24375BD4
    ParentResourceType = _AdditionalSliceInfo.ResourceType
    parent: _AdditionalSliceInfo
