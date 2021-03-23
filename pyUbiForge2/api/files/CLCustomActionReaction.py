from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLCustomActionReaction(SubclassBaseFile):
    ResourceType = 0x96BDCEED
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
