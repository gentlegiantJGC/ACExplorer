from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class GliderActor(SubclassBaseFile):
    ResourceType = 0x27BC81A8
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor
