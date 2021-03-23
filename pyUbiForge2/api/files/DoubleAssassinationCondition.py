from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class DoubleAssassinationCondition(SubclassBaseFile):
    ResourceType = 0xAB3AC976
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

