from pyUbiForge2.api.game import SubclassBaseFile
from .ProgressionCameraTransition import ProgressionCameraTransition as _ProgressionCameraTransition


class TemporalCameraTransition(SubclassBaseFile):
    ResourceType = 0xF042235F
    ParentResourceType = _ProgressionCameraTransition.ResourceType
    parent: _ProgressionCameraTransition

