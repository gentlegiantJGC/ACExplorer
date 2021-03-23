from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLHorseFollowMaster(SubclassBaseFile):
    ResourceType = 0x634A43EC
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

