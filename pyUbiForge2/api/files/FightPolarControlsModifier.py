from pyUbiForge2.api.game import SubclassBaseFile
from .PolarControlsModifier import PolarControlsModifier as _PolarControlsModifier


class FightPolarControlsModifier(SubclassBaseFile):
    ResourceType = 0x42EAA044
    ParentResourceType = _PolarControlsModifier.ResourceType
    parent: _PolarControlsModifier
