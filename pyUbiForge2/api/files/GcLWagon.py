from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLWagon(SubclassBaseFile):
    ResourceType = 0x88E0EDDD
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
