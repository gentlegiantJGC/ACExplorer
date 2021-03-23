from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class HayStackGrabAndKillEventMonitor(SubclassBaseFile):
    ResourceType = 0x95C2E4B2
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor

