from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLAssassin(SubclassBaseFile):
    ResourceType = 0x8EFA485B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

