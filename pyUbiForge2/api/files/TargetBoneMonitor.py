from pyUbiForge2.api.game import SubclassBaseFile
from .TargetMonitor import TargetMonitor as _TargetMonitor


class TargetBoneMonitor(SubclassBaseFile):
    ResourceType = 0x0525DFA2
    ParentResourceType = _TargetMonitor.ResourceType
    parent: _TargetMonitor

