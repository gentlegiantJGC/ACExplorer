from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLHorseInterceptEntityOnPath(SubclassBaseFile):
    ResourceType = 0x9C5C2506
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
