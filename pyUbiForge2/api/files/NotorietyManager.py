from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class NotorietyManager(SubclassBaseFile):
    ResourceType = 0x4C325D94
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
