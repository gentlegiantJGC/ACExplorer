from pyUbiForge2.api.game import SubclassBaseFile
from .AISerializedManager import AISerializedManager as _AISerializedManager


class HeadButtonCameraManager(SubclassBaseFile):
    ResourceType = 0xCF7BDCC2
    ParentResourceType = _AISerializedManager.ResourceType
    parent: _AISerializedManager

