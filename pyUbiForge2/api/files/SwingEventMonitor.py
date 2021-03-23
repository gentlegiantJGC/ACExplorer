from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class SwingEventMonitor(SubclassBaseFile):
    ResourceType = 0x749164A0
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
