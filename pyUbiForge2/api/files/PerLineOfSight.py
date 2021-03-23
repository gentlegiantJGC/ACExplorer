from pyUbiForge2.api.game import SubclassBaseFile
from .PerceptionToggle import PerceptionToggle as _PerceptionToggle


class PerLineOfSight(SubclassBaseFile):
    ResourceType = 0x32B0F96D
    ParentResourceType = _PerceptionToggle.ResourceType
    parent: _PerceptionToggle

