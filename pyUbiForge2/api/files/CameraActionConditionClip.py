from pyUbiForge2.api.game import SubclassBaseFile
from .ZoneConditionClip import ZoneConditionClip as _ZoneConditionClip


class CameraActionConditionClip(SubclassBaseFile):
    ResourceType = 0xAD57403E
    ParentResourceType = _ZoneConditionClip.ResourceType
    parent: _ZoneConditionClip

