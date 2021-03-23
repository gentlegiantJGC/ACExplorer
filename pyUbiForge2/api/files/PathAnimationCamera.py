from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class PathAnimationCamera(SubclassBaseFile):
    ResourceType = 0x1BE0C83E
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2
