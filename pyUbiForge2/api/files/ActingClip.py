from pyUbiForge2.api.game import SubclassBaseFile
from .TimedClip import TimedClip as _TimedClip


class ActingClip(SubclassBaseFile):
    ResourceType = 0xF4928EE7
    ParentResourceType = _TimedClip.ResourceType
    parent: _TimedClip

