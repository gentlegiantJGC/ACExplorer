from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFollowInFormation(SubclassBaseFile):
    ResourceType = 0x41DAA3CD
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

