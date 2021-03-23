from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLHorse(SubclassBaseFile):
    ResourceType = 0xE1C77FF3
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
