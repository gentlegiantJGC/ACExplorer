from pyUbiForge2.api.game import SubclassBaseFile
from .TargetBoneMonitor import TargetBoneMonitor as _TargetBoneMonitor


class TargetLeftHandBoneMonitor(SubclassBaseFile):
    ResourceType = 0xA0B06F2E
    ParentResourceType = _TargetBoneMonitor.ResourceType
    parent: _TargetBoneMonitor

