from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class BrokenStructureEventMonitor(SubclassBaseFile):
    ResourceType = 0xDBE02B97
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

