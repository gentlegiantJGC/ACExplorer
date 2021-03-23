from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerKillTargetMethodCondition(SubclassBaseFile):
    ResourceType = 0x925A0966
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
