from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLCollect(SubclassBaseFile):
    ResourceType = 0x72E79A7A
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

