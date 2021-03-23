from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class EavesdroppingEventMonitor(SubclassBaseFile):
    ResourceType = 0xA57EA5BA
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
