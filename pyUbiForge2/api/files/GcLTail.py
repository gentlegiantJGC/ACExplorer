from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLTail(SubclassBaseFile):
    ResourceType = 0xF2E2984A
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
