from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class GhostCameraEventMonitor(SubclassBaseFile):
    ResourceType = 0x9FC8336A
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

