from pyUbiForge2.api.game import SubclassBaseFile
from .SelfPreservationMode import SelfPreservationMode as _SelfPreservationMode


class FleeMode(SubclassBaseFile):
    ResourceType = 0xD99163CF
    ParentResourceType = _SelfPreservationMode.ResourceType
    parent: _SelfPreservationMode

