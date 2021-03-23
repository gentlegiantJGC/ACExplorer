from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class SwimEventMonitor(SubclassBaseFile):
    ResourceType = 0x7DC50563
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
