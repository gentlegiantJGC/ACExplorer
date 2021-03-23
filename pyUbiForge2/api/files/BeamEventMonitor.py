from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class BeamEventMonitor(SubclassBaseFile):
    ResourceType = 0xEA379A84
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
