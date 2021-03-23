from pyUbiForge2.api.game import SubclassBaseFile
from .AIActor import AIActor as _AIActor


class HorseHitchActor(SubclassBaseFile):
    ResourceType = 0xE8CF951D
    ParentResourceType = _AIActor.ResourceType
    parent: _AIActor

