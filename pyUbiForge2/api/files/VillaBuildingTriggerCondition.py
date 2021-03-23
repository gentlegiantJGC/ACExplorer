from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class VillaBuildingTriggerCondition(SubclassBaseFile):
    ResourceType = 0x0CFD1C74
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

