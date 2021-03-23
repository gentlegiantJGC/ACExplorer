from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class MilitaryOpenConflictTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x5243C856
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
