from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class TargetRidableBeastEntityMonitor(SubclassBaseFile):
    ResourceType = 0x73309B55
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
