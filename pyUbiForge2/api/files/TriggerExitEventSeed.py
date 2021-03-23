from pyUbiForge2.api.game import SubclassBaseFile
from .TriggerEventSeed import TriggerEventSeed as _TriggerEventSeed


class TriggerExitEventSeed(SubclassBaseFile):
    ResourceType = 0xE0F5805B
    ParentResourceType = _TriggerEventSeed.ResourceType
    parent: _TriggerEventSeed

