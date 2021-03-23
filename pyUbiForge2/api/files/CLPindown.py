from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPindown(SubclassBaseFile):
    ResourceType = 0x68B3CDE0
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

