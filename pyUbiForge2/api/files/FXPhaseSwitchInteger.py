from pyUbiForge2.api.game import SubclassBaseFile
from .FXPhaseSwitch import FXPhaseSwitch as _FXPhaseSwitch


class FXPhaseSwitchInteger(SubclassBaseFile):
    ResourceType = 0x3EDFE09B
    ParentResourceType = _FXPhaseSwitch.ResourceType
    parent: _FXPhaseSwitch
