from pyUbiForge2.api.game import SubclassBaseFile
from .TargetBoneMonitor import TargetBoneMonitor as _TargetBoneMonitor


class TargetHeadBoneMonitor(SubclassBaseFile):
    ResourceType = 0xC48302D6
    ParentResourceType = _TargetBoneMonitor.ResourceType
    parent: _TargetBoneMonitor

