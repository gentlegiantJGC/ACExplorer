from pyUbiForge2.api.game import SubclassBaseFile
from .Consequence import Consequence as _Consequence


class WalkthroughConsequence(SubclassBaseFile):
    ResourceType = 0x89E7E312
    ParentResourceType = _Consequence.ResourceType
    parent: _Consequence

