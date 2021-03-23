from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class ThrowRockTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x33F0D71D
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
