from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerInOddZoneCondition(SubclassBaseFile):
    ResourceType = 0x3AEDA294
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

