from pyUbiForge2.api.game import SubclassBaseFile
from .AICondition import AICondition as _AICondition


class CodexStateCondition(SubclassBaseFile):
    ResourceType = 0x9D09D195
    ParentResourceType = _AICondition.ResourceType
    parent: _AICondition

