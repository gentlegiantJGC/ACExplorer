from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class RopeEventMonitor(SubclassBaseFile):
    ResourceType = 0xCAA1D77B
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
