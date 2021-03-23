from pyUbiForge2.api.game import SubclassBaseFile
from .GameMenu import GameMenu as _GameMenu


class LoadWorldMenu(SubclassBaseFile):
    ResourceType = 0xB02B7BEE
    ParentResourceType = _GameMenu.ResourceType
    parent: _GameMenu

