from pyUbiForge2.api.game import SubclassBaseFile
from .ObservationMode import ObservationMode as _ObservationMode


class WatchMode(SubclassBaseFile):
    ResourceType = 0xC5C21AFD
    ParentResourceType = _ObservationMode.ResourceType
    parent: _ObservationMode
