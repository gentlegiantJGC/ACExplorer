from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSearch(SubclassBaseFile):
    ResourceType = 0x43057A58
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
