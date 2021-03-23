from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class VanishingManager(SubclassBaseFile):
    ResourceType = 0x30DD45CD
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

