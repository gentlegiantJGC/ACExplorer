from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class AssassinationTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0x2E8F6878
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

