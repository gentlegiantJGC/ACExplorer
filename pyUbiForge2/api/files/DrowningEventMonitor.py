from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class DrowningEventMonitor(SubclassBaseFile):
    ResourceType = 0xB287AB55
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

