from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class OptionsMenu(SubclassBaseFile):
    ResourceType = 0xB794729C
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
