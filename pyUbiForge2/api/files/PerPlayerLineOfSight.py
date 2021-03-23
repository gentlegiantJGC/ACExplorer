from pyUbiForge2.api.game import SubclassBaseFile
from .Perception import Perception as _Perception


class PerPlayerLineOfSight(SubclassBaseFile):
    ResourceType = 0xECD9430C
    ParentResourceType = _Perception.ResourceType
    parent: _Perception
