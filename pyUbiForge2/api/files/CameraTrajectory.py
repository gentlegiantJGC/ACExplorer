from pyUbiForge2.api.game import SubclassBaseFile
from .Trajectory import Trajectory as _Trajectory


class CameraTrajectory(SubclassBaseFile):
    ResourceType = 0x2998D35B
    ParentResourceType = _Trajectory.ResourceType
    parent: _Trajectory
