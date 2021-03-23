from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class CoordinatorOutputCondition(SubclassBaseFile):
    ResourceType = 0xC52E26DF
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
