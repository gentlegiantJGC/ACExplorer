from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLLocateTarget(SubclassBaseFile):
    ResourceType = 0xD7BA3078
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

