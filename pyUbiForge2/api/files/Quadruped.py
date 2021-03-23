from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class Quadruped(SubclassBaseFile):
    ResourceType = 0x00636580
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor
