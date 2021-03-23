from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class ConflictLoopManager(SubclassBaseFile):
    ResourceType = 0xB707DC33
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

