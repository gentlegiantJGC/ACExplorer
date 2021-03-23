from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLSiegeCannon(SubclassBaseFile):
    ResourceType = 0x56248991
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
