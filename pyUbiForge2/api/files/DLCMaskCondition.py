from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class DLCMaskCondition(SubclassBaseFile):
    ResourceType = 0x7A9DF512
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
