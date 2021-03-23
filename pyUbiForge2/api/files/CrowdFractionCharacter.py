from pyUbiForge2.api.game import SubclassBaseFile
from .CrowdFractionMembers import CrowdFractionMembers as _CrowdFractionMembers


class CrowdFractionCharacter(SubclassBaseFile):
    ResourceType = 0x87E5B138
    ParentResourceType = _CrowdFractionMembers.ResourceType
    parent: _CrowdFractionMembers

