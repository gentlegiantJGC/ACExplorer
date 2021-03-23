from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class MissionFailedMenuComponent(SubclassBaseFile):
    ResourceType = 0xCE8904FB
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
