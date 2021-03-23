from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLGuardPost(SubclassBaseFile):
    ResourceType = 0xF0B85884
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

