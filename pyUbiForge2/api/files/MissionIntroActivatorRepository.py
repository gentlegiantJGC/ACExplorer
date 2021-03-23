from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class MissionIntroActivatorRepository(SubclassBaseFile):
    ResourceType = 0xB0FFD20C
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

