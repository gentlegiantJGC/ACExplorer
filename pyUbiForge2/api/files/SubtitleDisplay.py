from pyUbiForge2.api.game import SubclassBaseFile
from .FireItem import FireItem as _FireItem


class SubtitleDisplay(SubclassBaseFile):
    ResourceType = 0xC77F406B
    ParentResourceType = _FireItem.ResourceType
    parent: _FireItem
