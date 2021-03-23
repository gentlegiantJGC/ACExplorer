from pyUbiForge2.api.game import SubclassBaseFile
from .SliceInfo import SliceInfo as _SliceInfo


class AdditionalSliceInfo(SubclassBaseFile):
    ResourceType = 0x13649EC1
    ParentResourceType = _SliceInfo.ResourceType
    parent: _SliceInfo

