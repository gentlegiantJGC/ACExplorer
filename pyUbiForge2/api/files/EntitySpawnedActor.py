from pyUbiForge2.api.game import SubclassBaseFile
from .EntityActor import EntityActor as _EntityActor


class EntitySpawnedActor(SubclassBaseFile):
    ResourceType = 0x29289F48
    ParentResourceType = _EntityActor.ResourceType
    parent: _EntityActor
