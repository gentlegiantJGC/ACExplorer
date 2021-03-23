from pyUbiForge2.api.game import SubclassBaseFile
from .TriggerEventSeed import TriggerEventSeed as _TriggerEventSeed


class TriggerEnterEventSeed(SubclassBaseFile):
    ResourceType = 0xFDFEFA9F
    ParentResourceType = _TriggerEventSeed.ResourceType
    parent: _TriggerEventSeed

