from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class TimeOfDayCondition(SubclassBaseFile):
    ResourceType = 0x630AE0B9
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

