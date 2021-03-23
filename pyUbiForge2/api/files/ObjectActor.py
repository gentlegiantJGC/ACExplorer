from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class ObjectActor(SubclassBaseFile):
    ResourceType = 0xC318BA22
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor

