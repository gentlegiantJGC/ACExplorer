from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLCourtesanFlirt(SubclassBaseFile):
    ResourceType = 0x156DFEFE
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
