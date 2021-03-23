from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLOrator(SubclassBaseFile):
    ResourceType = 0xB08B39EE
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
