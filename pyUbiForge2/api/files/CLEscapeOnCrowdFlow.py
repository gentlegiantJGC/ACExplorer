from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLEscapeOnCrowdFlow(SubclassBaseFile):
    ResourceType = 0xD2D90421
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

