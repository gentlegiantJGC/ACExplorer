from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPlayerCarry(SubclassBaseFile):
    ResourceType = 0x58F55D34
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

