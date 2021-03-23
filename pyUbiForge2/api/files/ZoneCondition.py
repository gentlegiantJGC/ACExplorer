from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class ZoneCondition(SubclassBaseFile):
    ResourceType = 0x8A2588E8
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

