from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLArcherDetectNPC(SubclassBaseFile):
    ResourceType = 0x36F8BFDC
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

