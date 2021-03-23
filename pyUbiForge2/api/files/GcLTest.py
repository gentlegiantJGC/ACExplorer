from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLTest(SubclassBaseFile):
    ResourceType = 0x56AA521B
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
