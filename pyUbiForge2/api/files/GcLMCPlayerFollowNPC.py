from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLMCPlayerFollowNPC(SubclassBaseFile):
    ResourceType = 0x39029569
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
