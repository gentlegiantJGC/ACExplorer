from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLShopkeeper(SubclassBaseFile):
    ResourceType = 0x7D28B3BB
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
