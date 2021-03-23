from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class SecondaryTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x4063917E
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
