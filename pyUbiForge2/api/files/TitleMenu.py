from pyUbiForge2.api.game import SubclassBaseFile
from .GameMenu import GameMenu as _GameMenu


class TitleMenu(SubclassBaseFile):
    ResourceType = 0xCCA336D1
    ParentResourceType = _GameMenu.ResourceType
    parent: _GameMenu
