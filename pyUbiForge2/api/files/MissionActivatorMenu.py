from pyUbiForge2.api.game import SubclassBaseFile
from .GameMenu import GameMenu as _GameMenu


class MissionActivatorMenu(SubclassBaseFile):
    ResourceType = 0xC57B6B4A
    ParentResourceType = _GameMenu.ResourceType
    parent: _GameMenu
