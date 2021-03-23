from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPatrol(SubclassBaseFile):
    ResourceType = 0x3CA045D1
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

