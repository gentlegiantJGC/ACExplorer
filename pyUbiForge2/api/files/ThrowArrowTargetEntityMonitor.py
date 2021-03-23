from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class ThrowArrowTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x52F8BC39
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

