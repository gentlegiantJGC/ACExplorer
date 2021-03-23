from pyUbiForge2.api.game import SubclassBaseFile
from .TargetBoneMonitor import TargetBoneMonitor as _TargetBoneMonitor


class ClimbReferentialMonitor(SubclassBaseFile):
    ResourceType = 0x31279B8F
    ParentResourceType = _TargetBoneMonitor.ResourceType
    parent: _TargetBoneMonitor

