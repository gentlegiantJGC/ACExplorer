from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLBeatUp(SubclassBaseFile):
    ResourceType = 0xD5DC19A8
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
