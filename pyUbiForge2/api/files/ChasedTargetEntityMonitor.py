from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class ChasedTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x4A44FA04
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
