from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class KioskEventMonitor(SubclassBaseFile):
    ResourceType = 0x2A7D5B48
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

