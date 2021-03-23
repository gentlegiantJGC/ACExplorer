from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerKillOtherThanTargetCondition(SubclassBaseFile):
    ResourceType = 0xDC39DD45
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
