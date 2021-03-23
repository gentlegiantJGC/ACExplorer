from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPlayerStealNPC(SubclassBaseFile):
    ResourceType = 0x2682A6A6
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
