from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLRest(SubclassBaseFile):
    ResourceType = 0xD96F3DDB
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

