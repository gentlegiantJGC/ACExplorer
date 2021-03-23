from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class TargetMainBehaviorEntityMonitor(SubclassBaseFile):
    ResourceType = 0x7D6FE251
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

