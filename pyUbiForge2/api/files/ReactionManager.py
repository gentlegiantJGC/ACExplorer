from pyUbiForge2.api.game import SubclassBaseFile
from .AISerializedManager import AISerializedManager as _AISerializedManager


class ReactionManager(SubclassBaseFile):
    ResourceType = 0xF85C3B4F
    ParentResourceType = _AISerializedManager.ResourceType
    parent: _AISerializedManager

