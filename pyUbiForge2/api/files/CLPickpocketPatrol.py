from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLPickpocketPatrol(SubclassBaseFile):
    ResourceType = 0x24E4A40E
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
