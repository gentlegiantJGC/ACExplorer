from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSimpleFlee(SubclassBaseFile):
    ResourceType = 0x111B4F3E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

