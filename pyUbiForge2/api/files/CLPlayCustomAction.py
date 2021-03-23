from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPlayCustomAction(SubclassBaseFile):
    ResourceType = 0x76DED37C
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

