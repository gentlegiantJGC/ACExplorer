from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PlayerNotorietyCondition(SubclassBaseFile):
    ResourceType = 0x966D4860
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
