from pyUbiForge2.api.game import SubclassBaseFile
from .TargetEntityMonitor import TargetEntityMonitor as _TargetEntityMonitor


class DetectionTargetEntityMonitor(SubclassBaseFile):
    ResourceType = 0xF161D0CA
    ParentResourceType = _TargetEntityMonitor.ResourceType
    parent: _TargetEntityMonitor

