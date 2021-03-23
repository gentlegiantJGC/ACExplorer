from pyUbiForge2.api.game import SubclassBaseFile
from .FirstPersonCamera import FirstPersonCamera as _FirstPersonCamera


class EavesdroppingCamera(SubclassBaseFile):
    ResourceType = 0xDD1C1F11
    ParentResourceType = _FirstPersonCamera.ResourceType
    parent: _FirstPersonCamera

