from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class SubtitleDisplayComponent(SubclassBaseFile):
    ResourceType = 0x2A6970AE
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
