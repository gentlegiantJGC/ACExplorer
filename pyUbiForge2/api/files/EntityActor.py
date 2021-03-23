from pyUbiForge2.api.game import SubclassBaseFile
from .MultiEntityActor import MultiEntityActor as _MultiEntityActor


class EntityActor(SubclassBaseFile):
    ResourceType = 0x16C13F1A
    ParentResourceType = _MultiEntityActor.ResourceType
    parent: _MultiEntityActor
