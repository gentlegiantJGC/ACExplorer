from pyUbiForge2.api.game import SubclassBaseFile
from .AISerializedManager import AISerializedManager as _AISerializedManager


class RankManager(SubclassBaseFile):
    ResourceType = 0xC4A59FC7
    ParentResourceType = _AISerializedManager.ResourceType
    parent: _AISerializedManager
