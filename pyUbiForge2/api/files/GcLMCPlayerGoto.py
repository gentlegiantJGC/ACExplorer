from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLMCPlayerGoto(SubclassBaseFile):
    ResourceType = 0xDE0BFC13
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
