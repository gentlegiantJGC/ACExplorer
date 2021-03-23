from pyUbiForge2.api.game import SubclassBaseFile
from .SaveGameDataObject import SaveGameDataObject as _SaveGameDataObject


class AssassinSaveGameData(SubclassBaseFile):
    ResourceType = 0x94D6F8F1
    ParentResourceType = _SaveGameDataObject.ResourceType
    parent: _SaveGameDataObject
