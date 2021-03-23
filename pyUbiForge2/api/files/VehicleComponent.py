from pyUbiForge2.api.game import SubclassBaseFile
from .CharacterController import CharacterController as _CharacterController


class VehicleComponent(SubclassBaseFile):
    ResourceType = 0x2FE2127D
    ParentResourceType = _CharacterController.ResourceType
    parent: _CharacterController

