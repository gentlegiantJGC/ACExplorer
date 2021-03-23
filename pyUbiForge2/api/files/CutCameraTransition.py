from pyUbiForge2.api.game import SubclassBaseFile
from .ICameraTransition import ICameraTransition as _ICameraTransition


class CutCameraTransition(SubclassBaseFile):
    ResourceType = 0xD8196FAE
    ParentResourceType = _ICameraTransition.ResourceType
    parent: _ICameraTransition

