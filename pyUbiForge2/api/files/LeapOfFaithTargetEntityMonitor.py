from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class LeapOfFaithTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0xFEEA4474
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

