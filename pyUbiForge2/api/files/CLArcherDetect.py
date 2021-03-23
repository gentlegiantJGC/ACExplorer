from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLArcherDetect(SubclassBaseFile):
    ResourceType = 0x8EA96304
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
