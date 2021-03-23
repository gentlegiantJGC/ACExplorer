from pyUbiForge2.api.game import SubclassBaseFile
from .TrajectoryPoint import TrajectoryPoint as _TrajectoryPoint


class CameraTrajectoryPoint(SubclassBaseFile):
    ResourceType = 0xBA00422E
    ParentResourceType = _TrajectoryPoint.ResourceType
    parent: _TrajectoryPoint

