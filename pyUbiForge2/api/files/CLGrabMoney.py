from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLGrabMoney(SubclassBaseFile):
    ResourceType = 0x2CECF3F2
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

