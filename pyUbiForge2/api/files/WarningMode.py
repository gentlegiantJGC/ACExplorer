from pyUbiForge2.api.game import SubclassBaseFile
from .ObservationMode import ObservationMode as _ObservationMode


class WarningMode(SubclassBaseFile):
    ResourceType = 0x0E6DB417
    ParentResourceType = _ObservationMode.ResourceType
    parent: _ObservationMode

