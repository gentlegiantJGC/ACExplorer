from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class MilitaryOpenConflictEventMonitor(SubclassBaseFile):
    ResourceType = 0x7F6B7AD4
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
