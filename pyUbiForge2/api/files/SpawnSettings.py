from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class SpawnSettings(SubclassBaseFile):
    ResourceType = 0xF7010C1C
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
