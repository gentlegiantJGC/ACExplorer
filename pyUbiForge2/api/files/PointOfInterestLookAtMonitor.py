from pyUbiForge2.api.game import SubclassBaseFile
from .TargetBoneMonitor import TargetBoneMonitor as _TargetBoneMonitor


class PointOfInterestLookAtMonitor(SubclassBaseFile):
    ResourceType = 0xF8157C61
    ParentResourceType = _TargetBoneMonitor.ResourceType
    parent: _TargetBoneMonitor

