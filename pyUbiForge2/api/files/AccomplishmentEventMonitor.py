from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentMonitor import AccomplishmentMonitor as _AccomplishmentMonitor


class AccomplishmentEventMonitor(SubclassBaseFile):
    ResourceType = 0xDE912BC9
    ParentResourceType = _AccomplishmentMonitor.ResourceType
    parent: _AccomplishmentMonitor
