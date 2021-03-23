from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class RollEventMonitor(SubclassBaseFile):
    ResourceType = 0x017370D2
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
