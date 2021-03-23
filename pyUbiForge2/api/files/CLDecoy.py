from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLDecoy(SubclassBaseFile):
    ResourceType = 0xB0B348BC
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
