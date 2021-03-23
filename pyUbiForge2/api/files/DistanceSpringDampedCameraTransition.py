from pyUbiForge2.api.game import SubclassBaseFile
from .ProgressionCameraTransition import (
    ProgressionCameraTransition as _ProgressionCameraTransition,
)


class DistanceSpringDampedCameraTransition(SubclassBaseFile):
    ResourceType = 0x28AECF39
    ParentResourceType = _ProgressionCameraTransition.ResourceType
    parent: _ProgressionCameraTransition
