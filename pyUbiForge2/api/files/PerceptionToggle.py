from pyUbiForge2.api.game import SubclassBaseFile
from .Perception import Perception as _Perception


class PerceptionToggle(SubclassBaseFile):
    ResourceType = 0xED146E66
    ParentResourceType = _Perception.ResourceType
    parent: _Perception
