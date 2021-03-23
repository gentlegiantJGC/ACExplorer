from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPickpocketeer(SubclassBaseFile):
    ResourceType = 0x474E8B85
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
