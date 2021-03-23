from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFollow(SubclassBaseFile):
    ResourceType = 0x9FC1E58F
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

