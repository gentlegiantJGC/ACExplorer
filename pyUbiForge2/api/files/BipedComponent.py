from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterController import CharacterController as _CharacterController


class BipedComponent(SubclassBaseFile):
    ResourceType = 0x08C9B2F3
    ParentResourceType = _CharacterController.ResourceType
    parent: _CharacterController
