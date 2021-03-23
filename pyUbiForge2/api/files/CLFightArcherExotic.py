from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFightArcherExotic(SubclassBaseFile):
    ResourceType = 0x658D226E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
