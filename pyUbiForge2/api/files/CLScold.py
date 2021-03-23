from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLScold(SubclassBaseFile):
    ResourceType = 0x06299A8C
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
