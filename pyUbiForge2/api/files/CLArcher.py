from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLArcher(SubclassBaseFile):
    ResourceType = 0xCF5B228B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
