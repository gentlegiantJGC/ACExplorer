from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class WagonActor(SubclassBaseFile):
    ResourceType = 0x25E215C4
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor
