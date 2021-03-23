from pyUbiForge2.api.game import SubclassBaseFile
from .TimedClip import TimedClip as _TimedClip


class AnimateClip(SubclassBaseFile):
    ResourceType = 0xC8B7556B
    ParentResourceType = _TimedClip.ResourceType
    parent: _TimedClip

