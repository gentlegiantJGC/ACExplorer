from pyUbiForge2.api.game import SubclassBaseFile
from .FXPhaseSwitch import FXPhaseSwitch as _FXPhaseSwitch


class FXPhaseSwitchFloat(SubclassBaseFile):
    ResourceType = 0x21B24420
    ParentResourceType = _FXPhaseSwitch.ResourceType
    parent: _FXPhaseSwitch
