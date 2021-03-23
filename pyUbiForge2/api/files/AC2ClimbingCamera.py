from pyUbiForge2.api.game import SubclassBaseFile
from .MovementCompensationCamera import MovementCompensationCamera as _MovementCompensationCamera


class AC2ClimbingCamera(SubclassBaseFile):
    ResourceType = 0xD46258AB
    ParentResourceType = _MovementCompensationCamera.ResourceType
    parent: _MovementCompensationCamera

