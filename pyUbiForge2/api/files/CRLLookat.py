from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CRLLookat(SubclassBaseFile):
    ResourceType = 0xFA0FC606
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

