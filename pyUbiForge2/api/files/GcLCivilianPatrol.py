from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLCivilianPatrol(SubclassBaseFile):
    ResourceType = 0x3EAA4EA3
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
