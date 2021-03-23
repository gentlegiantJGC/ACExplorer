from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLWander(SubclassBaseFile):
    ResourceType = 0x064AC8B9
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
