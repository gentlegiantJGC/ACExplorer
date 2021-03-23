from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class GroupManipulationManager(SubclassBaseFile):
    ResourceType = 0xCD81133E
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
