from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class ThrowRockEventMonitor(SubclassBaseFile):
    ResourceType = 0xC1E0486C
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

