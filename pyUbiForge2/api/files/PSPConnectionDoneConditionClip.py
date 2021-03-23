from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class PSPConnectionDoneConditionClip(SubclassBaseFile):
    ResourceType = 0x3D68B835
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

