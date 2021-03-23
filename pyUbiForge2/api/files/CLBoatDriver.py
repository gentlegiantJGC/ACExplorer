from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLBoatDriver(SubclassBaseFile):
    ResourceType = 0x5A813DFE
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
