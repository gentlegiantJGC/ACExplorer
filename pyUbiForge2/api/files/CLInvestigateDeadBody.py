from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInvestigateDeadBody(SubclassBaseFile):
    ResourceType = 0x0DDFBD5E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
