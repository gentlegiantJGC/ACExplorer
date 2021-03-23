from pyUbiForge2.api.game import SubclassBaseFile
from .PerceptionToggle import PerceptionToggle as _PerceptionToggle


class PerDanger(SubclassBaseFile):
    ResourceType = 0x77DCFEE5
    ParentResourceType = _PerceptionToggle.ResourceType
    parent: _PerceptionToggle

