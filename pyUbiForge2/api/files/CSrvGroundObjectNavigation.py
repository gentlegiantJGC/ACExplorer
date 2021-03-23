from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class CSrvGroundObjectNavigation(SubclassBaseFile):
    ResourceType = 0xA1F16084
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

