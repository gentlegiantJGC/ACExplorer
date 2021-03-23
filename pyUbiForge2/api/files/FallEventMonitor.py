from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class FallEventMonitor(SubclassBaseFile):
    ResourceType = 0xDE161ABE
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
