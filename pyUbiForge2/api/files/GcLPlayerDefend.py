from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPlayerDefend(SubclassBaseFile):
    ResourceType = 0x92252CF7
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

