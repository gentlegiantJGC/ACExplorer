from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerUseLeapOfFaithCondition(SubclassBaseFile):
    ResourceType = 0x9523127E
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

