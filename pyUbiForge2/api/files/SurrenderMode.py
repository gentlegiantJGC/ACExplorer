from pyUbiForge2.api.game import SubclassBaseFile
from .SelfPreservationMode import SelfPreservationMode as _SelfPreservationMode


class SurrenderMode(SubclassBaseFile):
    ResourceType = 0x32D45115
    ParentResourceType = _SelfPreservationMode.ResourceType
    parent: _SelfPreservationMode

