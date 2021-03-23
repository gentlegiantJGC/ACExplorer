from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPickpocket(SubclassBaseFile):
    ResourceType = 0x4CC89D01
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
