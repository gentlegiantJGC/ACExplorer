from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLBeatUp(SubclassBaseFile):
    ResourceType = 0x1572DEF7
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
