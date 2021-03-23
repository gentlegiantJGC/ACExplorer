from pyUbiForge2.api.game import SubclassBaseFile
from .EntityActor import EntityActor as _EntityActor


class CharacterActor(SubclassBaseFile):
    ResourceType = 0x020965A6
    ParentResourceType = _EntityActor.ResourceType
    parent: _EntityActor
