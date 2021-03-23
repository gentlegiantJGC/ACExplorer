from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class InteractConditionClip(SubclassBaseFile):
    ResourceType = 0x99AA4B80
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
