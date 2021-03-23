from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLHarassers(SubclassBaseFile):
    ResourceType = 0xEE2B3494
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

