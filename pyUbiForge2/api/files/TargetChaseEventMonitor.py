from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class TargetChaseEventMonitor(SubclassBaseFile):
    ResourceType = 0x0A4DD6AE
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
