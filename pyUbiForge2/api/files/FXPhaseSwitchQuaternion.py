from pyUbiForge2.api.game import SubclassBaseFile
from .FXPhaseSwitch import FXPhaseSwitch as _FXPhaseSwitch


class FXPhaseSwitchQuaternion(SubclassBaseFile):
    ResourceType = 0x23A5CE37
    ParentResourceType = _FXPhaseSwitch.ResourceType
    parent: _FXPhaseSwitch

