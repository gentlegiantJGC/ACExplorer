from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLBodyGuard(SubclassBaseFile):
    ResourceType = 0x7014E9BB
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

