from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class AssassinationEventMonitor(SubclassBaseFile):
    ResourceType = 0x36246A62
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

