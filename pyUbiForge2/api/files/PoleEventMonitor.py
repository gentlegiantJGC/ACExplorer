from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class PoleEventMonitor(SubclassBaseFile):
    ResourceType = 0x01465F59
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
