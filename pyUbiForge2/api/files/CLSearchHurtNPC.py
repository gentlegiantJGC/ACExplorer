from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSearchHurtNPC(SubclassBaseFile):
    ResourceType = 0x0280E016
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

