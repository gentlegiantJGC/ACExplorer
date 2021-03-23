from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class BrokenStructureConditionClip(SubclassBaseFile):
    ResourceType = 0xF2CD0564
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

