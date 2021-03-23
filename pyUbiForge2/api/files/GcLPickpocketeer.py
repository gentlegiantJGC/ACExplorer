from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPickpocketeer(SubclassBaseFile):
    ResourceType = 0x2764F326
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

