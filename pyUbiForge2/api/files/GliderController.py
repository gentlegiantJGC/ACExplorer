from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterController import CharacterController as _CharacterController


class GliderController(SubclassBaseFile):
    ResourceType = 0x22AC946A
    ParentResourceType = _CharacterController.ResourceType
    parent: _CharacterController

