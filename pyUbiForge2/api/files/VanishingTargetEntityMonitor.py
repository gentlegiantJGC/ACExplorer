from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class VanishingTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0xAC09012C
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

