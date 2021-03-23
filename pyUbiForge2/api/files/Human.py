from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class Human(SubclassBaseFile):
    ResourceType = 0xA0A43252
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor
