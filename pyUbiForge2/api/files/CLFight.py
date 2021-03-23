from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFight(SubclassBaseFile):
    ResourceType = 0xB65CE6C2
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
