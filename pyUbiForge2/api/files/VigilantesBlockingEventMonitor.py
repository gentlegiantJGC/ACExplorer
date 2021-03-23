from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class VigilantesBlockingEventMonitor(SubclassBaseFile):
    ResourceType = 0xBDA88B49
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
