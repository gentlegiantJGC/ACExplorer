from pyUbiForge2.api.game import SubclassBaseFile
from .CuriosityMode import CuriosityMode as _CuriosityMode


class WalkAndLookAtMode(SubclassBaseFile):
    ResourceType = 0xE8D48C34
    ParentResourceType = _CuriosityMode.ResourceType
    parent: _CuriosityMode
