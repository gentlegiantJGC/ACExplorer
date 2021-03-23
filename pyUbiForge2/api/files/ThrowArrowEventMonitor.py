from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class ThrowArrowEventMonitor(SubclassBaseFile):
    ResourceType = 0x6367AAFF
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

