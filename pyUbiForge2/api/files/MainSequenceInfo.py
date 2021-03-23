from pyUbiForge2.api.game import SubclassBaseFile
from .SliceGroupInfo import SliceGroupInfo as _SliceGroupInfo


class MainSequenceInfo(SubclassBaseFile):
    ResourceType = 0xF9C2401B
    ParentResourceType = _SliceGroupInfo.ResourceType
    parent: _SliceGroupInfo
