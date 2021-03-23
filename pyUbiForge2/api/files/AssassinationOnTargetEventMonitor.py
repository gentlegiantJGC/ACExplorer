from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEventMonitor import TargetEventMonitor as _TargetEventMonitor


class AssassinationOnTargetEventMonitor(SubclassBaseFile):
    ResourceType = 0x1EDE58BD
    ParentResourceType = _TargetEventMonitor.ResourceType
    parent: _TargetEventMonitor
