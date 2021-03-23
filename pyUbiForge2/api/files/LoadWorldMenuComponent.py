from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class LoadWorldMenuComponent(SubclassBaseFile):
    ResourceType = 0x1FB18A58
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent

