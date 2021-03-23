from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLHorse(SubclassBaseFile):
    ResourceType = 0xF56C8D8C
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

