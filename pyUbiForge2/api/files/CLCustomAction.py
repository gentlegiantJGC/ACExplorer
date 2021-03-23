from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLCustomAction(SubclassBaseFile):
    ResourceType = 0xA1E5037B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

