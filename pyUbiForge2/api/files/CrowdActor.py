from pyUbiForge2.api.game import SubclassBaseFile
from .MultiEntityActor import MultiEntityActor as _MultiEntityActor


class CrowdActor(SubclassBaseFile):
    ResourceType = 0xB8A5A098
    ParentResourceType = _MultiEntityActor.ResourceType
    parent: _MultiEntityActor

