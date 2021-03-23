from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class FlythroughCondition(SubclassBaseFile):
    ResourceType = 0x8E96F44C
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

