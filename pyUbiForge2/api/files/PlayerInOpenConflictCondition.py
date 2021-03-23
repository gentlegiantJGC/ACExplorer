from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerInOpenConflictCondition(SubclassBaseFile):
    ResourceType = 0xC4CD4D09
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

