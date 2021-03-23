from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLGlider(SubclassBaseFile):
    ResourceType = 0x60DB362A
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

