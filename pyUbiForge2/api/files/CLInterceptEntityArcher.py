from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLInterceptEntityArcher(SubclassBaseFile):
    ResourceType = 0xFF3190C0
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
