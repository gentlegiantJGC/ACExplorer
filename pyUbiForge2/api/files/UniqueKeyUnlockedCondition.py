from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class UniqueKeyUnlockedCondition(SubclassBaseFile):
    ResourceType = 0xCBD0BDEF
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

