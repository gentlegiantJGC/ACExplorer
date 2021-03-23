from pyUbiForge2.api.game import SubclassBaseFile
from .CollectibleDistrictInfo import CollectibleDistrictInfo as _CollectibleDistrictInfo


class RHPDistrictInfo(SubclassBaseFile):
    ResourceType = 0x1AFDE5D7
    ParentResourceType = _CollectibleDistrictInfo.ResourceType
    parent: _CollectibleDistrictInfo

