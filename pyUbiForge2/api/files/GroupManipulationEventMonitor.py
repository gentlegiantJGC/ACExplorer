from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class GroupManipulationEventMonitor(SubclassBaseFile):
    ResourceType = 0x7C30C488
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
