from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class ChasedEventMonitor(SubclassBaseFile):
    ResourceType = 0x623FAACF
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

