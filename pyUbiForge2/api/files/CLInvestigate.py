from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInvestigate(SubclassBaseFile):
    ResourceType = 0x03BD916A
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
