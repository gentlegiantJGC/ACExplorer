from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLArcher(SubclassBaseFile):
    ResourceType = 0x0FF5E5D4
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

