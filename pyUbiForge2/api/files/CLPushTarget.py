from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPushTarget(SubclassBaseFile):
    ResourceType = 0x89DD370D
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
