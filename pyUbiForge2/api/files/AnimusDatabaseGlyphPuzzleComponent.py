from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class AnimusDatabaseGlyphPuzzleComponent(SubclassBaseFile):
    ResourceType = 0x316232B4
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

