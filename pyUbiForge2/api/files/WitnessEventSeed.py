from pyUbiForge2.api.game import SubclassBaseFile
from .EventSeed import EventSeed as _EventSeed


class WitnessEventSeed(SubclassBaseFile):
    ResourceType = 0xFC27D415
    ParentResourceType = _EventSeed.ResourceType
    parent: _EventSeed
