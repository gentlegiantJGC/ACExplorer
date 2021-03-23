from pyUbiForge2.api.game import SubclassBaseFile
from .ActionFilterConditionClip import (
    ActionFilterConditionClip as _ActionFilterConditionClip,
)


class ZoneConditionClip(SubclassBaseFile):
    ResourceType = 0x1461226F
    ParentResourceType = _ActionFilterConditionClip.ResourceType
    parent: _ActionFilterConditionClip
