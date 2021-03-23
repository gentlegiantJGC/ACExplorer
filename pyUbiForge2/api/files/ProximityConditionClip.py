from pyUbiForge2.api.game import SubclassBaseFile
from .ActionFilterConditionClip import (
    ActionFilterConditionClip as _ActionFilterConditionClip,
)


class ProximityConditionClip(SubclassBaseFile):
    ResourceType = 0xC2F06D0E
    ParentResourceType = _ActionFilterConditionClip.ResourceType
    parent: _ActionFilterConditionClip
