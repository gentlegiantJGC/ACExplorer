from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class VanishingEventMonitor(SubclassBaseFile):
    ResourceType = 0x5976F65F
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
