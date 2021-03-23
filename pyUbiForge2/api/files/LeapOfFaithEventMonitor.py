from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class LeapOfFaithEventMonitor(SubclassBaseFile):
    ResourceType = 0xD204A3ED
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
