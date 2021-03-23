from pyUbiForge2.api.game import SubclassBaseFile
from .EntityActor import EntityActor as _EntityActor


class EntityInventoryActor(SubclassBaseFile):
    ResourceType = 0xCB540239
    ParentResourceType = _EntityActor.ResourceType
    parent: _EntityActor
