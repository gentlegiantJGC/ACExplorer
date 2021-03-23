from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class BrokenStructureTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0xE44D7331
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

