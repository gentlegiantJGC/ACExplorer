from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSimpleFollow(SubclassBaseFile):
    ResourceType = 0xFF02D9BA
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
