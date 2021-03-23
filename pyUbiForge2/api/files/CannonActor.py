from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class CannonActor(SubclassBaseFile):
    ResourceType = 0x475E9535
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor

