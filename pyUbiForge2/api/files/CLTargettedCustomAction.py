from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLTargettedCustomAction(SubclassBaseFile):
    ResourceType = 0x6F9A4D19
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

