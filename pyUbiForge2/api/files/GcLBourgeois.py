from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLBourgeois(SubclassBaseFile):
    ResourceType = 0x6AD995CE
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

