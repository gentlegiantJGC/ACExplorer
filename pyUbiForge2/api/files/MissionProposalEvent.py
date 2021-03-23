from pyUbiForge2.api.game import SubclassBaseFile
from .MissionEvent import MissionEvent as _MissionEvent


class MissionProposalEvent(SubclassBaseFile):
    ResourceType = 0xA3987430
    ParentResourceType = _MissionEvent.ResourceType
    parent: _MissionEvent

