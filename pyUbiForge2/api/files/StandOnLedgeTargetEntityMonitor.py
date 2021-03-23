from pyUbiForge2.api.game import SubclassBaseFile
from .TargetObjectMonitor import TargetObjectMonitor as _TargetObjectMonitor


class StandOnLedgeTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0xFE163C5A
    ParentResourceType = _TargetObjectMonitor.ResourceType
    parent: _TargetObjectMonitor

