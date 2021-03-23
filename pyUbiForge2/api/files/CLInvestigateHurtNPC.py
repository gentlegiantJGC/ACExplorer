from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInvestigateHurtNPC(SubclassBaseFile):
    ResourceType = 0xFA5CA4C4
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

