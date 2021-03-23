from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvMilitaryCrowdInteraction(SubclassBaseFile):
    ResourceType = 0x25273340
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

