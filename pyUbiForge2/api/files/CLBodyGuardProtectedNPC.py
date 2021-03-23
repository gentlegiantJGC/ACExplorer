from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLBodyGuardProtectedNPC(SubclassBaseFile):
    ResourceType = 0x57FBD569
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
