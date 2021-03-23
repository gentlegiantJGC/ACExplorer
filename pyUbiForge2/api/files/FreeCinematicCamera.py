from pyUbiForge2.api.game import SubclassBaseFile
from .Camera import Camera as _Camera


class FreeCinematicCamera(SubclassBaseFile):
    ResourceType = 0x4F7817C7
    ParentResourceType = _Camera.ResourceType
    parent: _Camera
