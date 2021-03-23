from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class VillaTriggerCondition(SubclassBaseFile):
    ResourceType = 0xEED29252
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

