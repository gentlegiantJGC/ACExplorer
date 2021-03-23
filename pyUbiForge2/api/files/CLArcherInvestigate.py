from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLArcherInvestigate(SubclassBaseFile):
    ResourceType = 0x1E898A16
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
