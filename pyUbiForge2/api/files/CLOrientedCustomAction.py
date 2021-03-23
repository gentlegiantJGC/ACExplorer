from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLOrientedCustomAction(SubclassBaseFile):
    ResourceType = 0x7C0D763D
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

