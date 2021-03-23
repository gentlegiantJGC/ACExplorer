from pyUbiForge2.api.game import SubclassBaseFile
from .Consequence import Consequence as _Consequence


class ChangeWorldConsequence(SubclassBaseFile):
    ResourceType = 0x72B1E74D
    ParentResourceType = _Consequence.ResourceType
    parent: _Consequence
