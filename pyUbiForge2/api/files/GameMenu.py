from pyUbiForge2.api.game import SubclassBaseFile
from .FireItem import FireItem as _FireItem


class GameMenu(SubclassBaseFile):
    ResourceType = 0x7270FDC4
    ParentResourceType = _FireItem.ResourceType
    parent: _FireItem

