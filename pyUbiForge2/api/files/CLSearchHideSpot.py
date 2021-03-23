from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLSearchHideSpot(SubclassBaseFile):
    ResourceType = 0xFAC2641B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

