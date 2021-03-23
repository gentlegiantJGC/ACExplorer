from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class BoatDrivingEventMonitor(SubclassBaseFile):
    ResourceType = 0x097F725C
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
