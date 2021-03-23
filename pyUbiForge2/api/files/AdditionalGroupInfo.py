from pyUbiForge2.api.game import SubclassBaseFile
from .SliceGroupInfo import SliceGroupInfo as _SliceGroupInfo


class AdditionalGroupInfo(SubclassBaseFile):
    ResourceType = 0x952662EB
    ParentResourceType = _SliceGroupInfo.ResourceType
    parent: _SliceGroupInfo

