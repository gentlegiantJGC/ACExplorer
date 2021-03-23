from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLBourgeoisFlee(SubclassBaseFile):
    ResourceType = 0x0B598D11
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

