from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLTargetInvestigate(SubclassBaseFile):
    ResourceType = 0x76A9203A
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
