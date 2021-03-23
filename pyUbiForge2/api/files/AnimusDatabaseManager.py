from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class AnimusDatabaseManager(SubclassBaseFile):
    ResourceType = 0x8C7A01C7
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

