from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class WorldAmbianceManager(SubclassBaseFile):
    ResourceType = 0x4C9AF0FE
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
