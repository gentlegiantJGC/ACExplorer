from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class AccomplishmentCondition(SubclassBaseFile):
    ResourceType = 0x3EB1853F
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
