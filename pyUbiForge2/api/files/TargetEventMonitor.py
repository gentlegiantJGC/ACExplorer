from pyUbiForge2.api.game import SubclassBaseFile
from .TargetMonitor import TargetMonitor as _TargetMonitor


class TargetEventMonitor(SubclassBaseFile):
    ResourceType = 0x79F2AEF4
    ParentResourceType = _TargetMonitor.ResourceType
    parent: _TargetMonitor

