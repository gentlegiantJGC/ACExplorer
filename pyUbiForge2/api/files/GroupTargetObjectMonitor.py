from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class GroupTargetObjectMonitor(SubclassBaseFile):
    ResourceType = 0xC749EA9F
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor
