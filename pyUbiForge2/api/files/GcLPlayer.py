from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPlayer(SubclassBaseFile):
    ResourceType = 0xAF421CC5
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

