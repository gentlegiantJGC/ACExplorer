from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPlayerDeath(SubclassBaseFile):
    ResourceType = 0x0EF8A5AF
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

