from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class ClimbTopLedgeEventMonitor(SubclassBaseFile):
    ResourceType = 0xEA9B545E
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

