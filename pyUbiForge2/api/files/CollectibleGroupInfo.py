from pyUbiForge2.api.game import SubclassBaseFile
from .AdditionalGroupInfo import AdditionalGroupInfo as _AdditionalGroupInfo


class CollectibleGroupInfo(SubclassBaseFile):
    ResourceType = 0xA275A7FE
    ParentResourceType = _AdditionalGroupInfo.ResourceType
    parent: _AdditionalGroupInfo

