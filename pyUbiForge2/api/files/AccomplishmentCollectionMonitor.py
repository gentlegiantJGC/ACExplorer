from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentMonitor import AccomplishmentMonitor as _AccomplishmentMonitor


class AccomplishmentCollectionMonitor(SubclassBaseFile):
    ResourceType = 0x5C21AFD3
    ParentResourceType = _AccomplishmentMonitor.ResourceType
    parent: _AccomplishmentMonitor
