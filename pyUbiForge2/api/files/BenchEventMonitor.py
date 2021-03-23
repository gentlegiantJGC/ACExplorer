from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class BenchEventMonitor(SubclassBaseFile):
    ResourceType = 0x8E6A8717
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
