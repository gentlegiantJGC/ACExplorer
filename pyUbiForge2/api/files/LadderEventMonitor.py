from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class LadderEventMonitor(SubclassBaseFile):
    ResourceType = 0x442EBE3E
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

