from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLAmbushWagon(SubclassBaseFile):
    ResourceType = 0xAAD91C01
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

