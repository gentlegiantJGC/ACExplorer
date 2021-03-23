from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PausePatrolEvent(SubclassBaseFile):
    ResourceType = 0x3D005C8D
    ParentResourceType = _Event.ResourceType
    parent: _Event
