from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CRLCustomAction(SubclassBaseFile):
    ResourceType = 0x87B6B545
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

