from pyUbiForge2.api.game import SubclassBaseFile
from .Perception import Perception as _Perception


class PerFight(SubclassBaseFile):
    ResourceType = 0x89297F68
    ParentResourceType = _Perception.ResourceType
    parent: _Perception

