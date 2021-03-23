from pyUbiForge2.api.game import SubclassBaseFile
from .GameMenu import GameMenu as _GameMenu


class PauseMenu(SubclassBaseFile):
    ResourceType = 0x165DC792
    ParentResourceType = _GameMenu.ResourceType
    parent: _GameMenu
