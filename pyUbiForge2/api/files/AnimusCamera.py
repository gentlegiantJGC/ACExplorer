from pyUbiForge2.api.game import SubclassBaseFile
from .FixedCamera import FixedCamera as _FixedCamera


class AnimusCamera(SubclassBaseFile):
    ResourceType = 0xE62DD655
    ParentResourceType = _FixedCamera.ResourceType
    parent: _FixedCamera
