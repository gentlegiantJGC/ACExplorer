from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class GroupWaitCondition(SubclassBaseFile):
    ResourceType = 0x2E34547D
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
