from pyUbiForge2.api.game import SubclassBaseFile
from .FXPhaseSwitch import FXPhaseSwitch as _FXPhaseSwitch


class FXPhaseSwitchVector(SubclassBaseFile):
    ResourceType = 0xA08D1842
    ParentResourceType = _FXPhaseSwitch.ResourceType
    parent: _FXPhaseSwitch

