from pyUbiForge2.api.game import SubclassBaseFile
from .ICameraTransition import ICameraTransition as _ICameraTransition


class ProgressionCameraTransition(SubclassBaseFile):
    ResourceType = 0x8300E0FB
    ParentResourceType = _ICameraTransition.ResourceType
    parent: _ICameraTransition

