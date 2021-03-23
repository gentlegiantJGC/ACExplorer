from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class TargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x3CA5750E
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
