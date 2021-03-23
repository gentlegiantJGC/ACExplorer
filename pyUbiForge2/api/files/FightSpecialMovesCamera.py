from pyUbiForge2.api.game import SubclassBaseFile
from .InsertCamera import InsertCamera as _InsertCamera


class FightSpecialMovesCamera(SubclassBaseFile):
    ResourceType = 0xFF2C552A
    ParentResourceType = _InsertCamera.ResourceType
    parent: _InsertCamera

