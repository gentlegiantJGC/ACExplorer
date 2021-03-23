from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLBlockingGuards(SubclassBaseFile):
    ResourceType = 0xE178AFDB
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
