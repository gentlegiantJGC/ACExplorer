from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPlayerEscape(SubclassBaseFile):
    ResourceType = 0x2548CAD7
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
