from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLKillTarget(SubclassBaseFile):
    ResourceType = 0xE1DD3705
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
