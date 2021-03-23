from pyUbiForge2.api.game import SubclassBaseFile
from .AISerializedManager import AISerializedManager as _AISerializedManager


class SaveGameDataManager(SubclassBaseFile):
    ResourceType = 0x575C803B
    ParentResourceType = _AISerializedManager.ResourceType
    parent: _AISerializedManager
