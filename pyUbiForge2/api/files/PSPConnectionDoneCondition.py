from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class PSPConnectionDoneCondition(SubclassBaseFile):
    ResourceType = 0x14F70B09
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition
