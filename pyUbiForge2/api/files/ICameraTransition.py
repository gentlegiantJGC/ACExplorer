from pyUbiForge2.api.game import SubclassBaseFile
from .Camera2 import Camera2 as _Camera2


class ICameraTransition(SubclassBaseFile):
    ResourceType = 0x237EC0C7
    ParentResourceType = _Camera2.ResourceType
    parent: _Camera2
