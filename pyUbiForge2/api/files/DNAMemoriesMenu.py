from pyUbiForge2.api.game import SubclassBaseFile
from .FireItemComponent import FireItemComponent as _FireItemComponent


class DNAMemoriesMenu(SubclassBaseFile):
    ResourceType = 0xBF826BEB
    ParentResourceType = _FireItemComponent.ResourceType
    parent: _FireItemComponent
