from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class ClimbEventMonitor(SubclassBaseFile):
    ResourceType = 0xBE727E36
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

