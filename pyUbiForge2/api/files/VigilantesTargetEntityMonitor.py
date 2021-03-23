from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class VigilantesTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0xB8BFD457
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

