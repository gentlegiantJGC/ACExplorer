from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvFleeToCrowd(SubclassBaseFile):
    ResourceType = 0x83A7A1DD
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
