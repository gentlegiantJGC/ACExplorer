from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterController import CharacterController as _CharacterController


class QuadrupedComponent(SubclassBaseFile):
    ResourceType = 0x8F0FDB1C
    ParentResourceType = _CharacterController.ResourceType
    parent: _CharacterController

