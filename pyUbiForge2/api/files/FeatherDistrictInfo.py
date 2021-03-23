from pyUbiForge2.api.game import SubclassBaseFile
from .CollectibleDistrictInfo import CollectibleDistrictInfo as _CollectibleDistrictInfo


class FeatherDistrictInfo(SubclassBaseFile):
    ResourceType = 0x39C328FA
    ParentResourceType = _CollectibleDistrictInfo.ResourceType
    parent: _CollectibleDistrictInfo
