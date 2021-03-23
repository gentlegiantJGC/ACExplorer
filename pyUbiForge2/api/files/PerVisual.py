from pyUbiForge2.api.game import SubclassBaseFile
from .PerceptionToggle import PerceptionToggle as _PerceptionToggle


class PerVisual(SubclassBaseFile):
    ResourceType = 0x2A00168F
    ParentResourceType = _PerceptionToggle.ResourceType
    parent: _PerceptionToggle

