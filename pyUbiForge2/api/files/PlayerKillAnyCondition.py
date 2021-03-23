from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerKillAnyCondition(SubclassBaseFile):
    ResourceType = 0xC87BB9E6
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

