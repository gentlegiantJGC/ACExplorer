from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class StandOnLedgeEventMonitor(SubclassBaseFile):
    ResourceType = 0xEFC0C29E
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

