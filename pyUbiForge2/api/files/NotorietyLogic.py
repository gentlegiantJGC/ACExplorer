from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class NotorietyLogic(SubclassBaseFile):
    ResourceType = 0xEB5D07A8
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

