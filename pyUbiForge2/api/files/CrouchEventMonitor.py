from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class CrouchEventMonitor(SubclassBaseFile):
    ResourceType = 0x27423CFF
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
