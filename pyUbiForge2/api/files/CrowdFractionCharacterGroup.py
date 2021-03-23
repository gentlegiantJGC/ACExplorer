from pyUbiForge2.api.game import SubclassBaseFile
from .CrowdFractionMembers import CrowdFractionMembers as _CrowdFractionMembers


class CrowdFractionCharacterGroup(SubclassBaseFile):
    ResourceType = 0x4375ADBE
    ParentResourceType = _CrowdFractionMembers.ResourceType
    parent: _CrowdFractionMembers
