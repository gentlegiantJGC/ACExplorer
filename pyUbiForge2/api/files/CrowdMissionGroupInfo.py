from pyUbiForge2.api.game import SubclassBaseFile
from .AdditionalGroupInfo import AdditionalGroupInfo as _AdditionalGroupInfo


class CrowdMissionGroupInfo(SubclassBaseFile):
    ResourceType = 0x31445C8A
    ParentResourceType = _AdditionalGroupInfo.ResourceType
    parent: _AdditionalGroupInfo

