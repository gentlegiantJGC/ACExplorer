from pyUbiForge2.api.game import SubclassBaseFile
from .AISerializedManager import AISerializedManager as _AISerializedManager


class CameraSecondaryTargetManager(SubclassBaseFile):
    ResourceType = 0x1D9546FE
    ParentResourceType = _AISerializedManager.ResourceType
    parent: _AISerializedManager
