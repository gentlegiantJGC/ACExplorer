from pyUbiForge2.api.game import SubclassBaseFile
from .SaveGameDataObject import SaveGameDataObject as _SaveGameDataObject


class AssassinGlobalProfileData(SubclassBaseFile):
    ResourceType = 0x305AE1A8
    ParentResourceType = _SaveGameDataObject.ResourceType
    parent: _SaveGameDataObject

