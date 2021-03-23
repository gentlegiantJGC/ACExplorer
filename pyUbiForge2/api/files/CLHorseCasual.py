from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLHorseCasual(SubclassBaseFile):
    ResourceType = 0x6DF50CC0
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

