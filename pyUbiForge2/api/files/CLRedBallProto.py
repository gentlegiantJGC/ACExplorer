from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLRedBallProto(SubclassBaseFile):
    ResourceType = 0x116E50B0
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
