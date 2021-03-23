from pyUbiForge2.api.game import SubclassBaseFile
from .InsertCamera import InsertCamera as _InsertCamera


class AssassinationCamera(SubclassBaseFile):
    ResourceType = 0xCB29B8E5
    ParentResourceType = _InsertCamera.ResourceType
    parent: _InsertCamera
